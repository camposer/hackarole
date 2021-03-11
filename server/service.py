import logging
import os
import strongdm

import model

client = strongdm.Client(
    os.getenv("SDM_API_ACCESS_KEY"), 
    os.getenv("SDM_API_SECRET_KEY")
)

def save_user_resources(users: [model.User]):
    for user in users:
        sdm_user = get_or_create_user(user)
        logging.info("User details %s", sdm_user)
    
        for resource in user.resources_to_grant:
            sdm_resource = grant_resource(sdm_user, resource)
            if sdm_resource:
                logging.info("Resource = %s granted to user = %s", sdm_resource, sdm_user)

        for resource in user.resources_to_revoke:
            sdm_resource = revoke_resource(sdm_user, resource)
            if sdm_resource:
                logging.info("Resource = %s revoked from user = %s", sdm_resource, sdm_user)


def get_or_create_user(user: model.User):
    sdm_user = next(client.accounts.list(f'email:{user.email}'), None)
    if not sdm_user:
        new_user = strongdm.User(
            email = user.email,
            first_name = user.first_name,
            last_name = user.last_name,
        )
        response = client.accounts.create(new_user, timeout=30)
        sdm_user = response.account
    return sdm_user


def grant_resource(sdm_user, resource: model.Resource):  
    sdm_resource = get_resource(sdm_user, resource)   
    if not sdm_resource:
        return None
    grant = strongdm.AccountGrant(
        account_id = sdm_user.id,
        resource_id = sdm_resource.id,
    )
    if get_grant(sdm_user, sdm_resource):
        return None
    response = client.account_grants.create(grant, timeout=30)
    return response.account_grant

def get_resource(sdm_user, resource: model.Resource):
    for sdm_resource in client.resources.list(f'name:{resource.name}'):
        logging.debug("Found resource %s for the name %s", sdm_resource, resource.name)
        if type(sdm_resource) is resource.type.value:
            logging.debug("Type matches %s", sdm_resource)
            return sdm_resource
        else:
            logging.debug("Type doesn't match %s", sdm_resource)
    return None


def get_grant(sdm_user, sdm_resource):
    return next(client.account_grants.list(f'account_id:{sdm_user.id},resource_id:{sdm_resource.id}'), None)


def revoke_resource(sdm_user, resource: model.Resource):
    sdm_resource = get_resource(sdm_user, resource)   
    if not sdm_resource:
        return None
    account_grant = get_grant(sdm_user, sdm_resource)
    if not account_grant:
        return None
    client.account_grants.delete(account_grant.id, timeout=30)
    return account_grant
