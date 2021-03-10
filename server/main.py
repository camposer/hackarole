import logging

from model import User, Resource, ResourceType
import service

logging.basicConfig(level=logging.INFO)

def main():
    resource_postgres = Resource("rodo-eks-db", ResourceType.POSTGRES)
    resource_ssh = Resource("fake-ssh", ResourceType.SSHCert)
    resource_invalid = Resource("non-existy", ResourceType.SSHCert)

    users = [
        User("user1@example.com", "User1", "Test", [resource_postgres], []),
        User("user2@example.com", "User2", "Test", [resource_ssh], []),
        User("user3@example.com", "User3", "Test", [resource_invalid], [])
    ]
    print("Saving user resources")
    print(users)
    service.save_user_resources(users)

    print()

    users = [
        User("user1@example.com", "User1", "Test", [resource_ssh], [resource_postgres, resource_invalid]),
        User("user2@example.com", "User2", "Test", [resource_postgres], [resource_ssh]),
        User("user3@example.com", "User3", "Test", [], [resource_postgres])
    ]
    print("Saving user resources")
    print(users)
    service.save_user_resources(users)


if __name__ == "__main__":
    main()