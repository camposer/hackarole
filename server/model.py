from enum import Enum 
import strongdm

class User:
    def __init__(self, email, first_name, last_name, resources_to_grant, resources_to_revoke):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.resources_to_grant = resources_to_grant
        self.resources_to_revoke = resources_to_revoke

    def __str__(self):
        return f"email = {self.email} resources_to_grant = {self.resources_to_grant} resources_to_revoke = {self.resources_to_revoke}"

    def __repr__(self):
        return self.__str__()


# Complete list
class ResourceType(Enum):
    POSTGRES = strongdm.models.Postgres
    SSHCert = strongdm.models.SSHCert


class Resource:
    def __init__(self, name, type: ResourceType):
        self.name = name
        self.type = type

    def __str__(self):
        return f"name = {self.name} type = {self.type}"

    def __repr__(self):
        return self.__str__()
