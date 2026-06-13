class User:
    def __init__(self, name:str):
        self.name = name
        self.groups = []
    
    def add_group(self, group:Group):
        self.groups.append(group)
        group.add_user(self)

class Group:
    def __init__(self, name:str):
        self.name = name
        self.users = []
    
    def add_user(self, user:User):
        self.users.append(user)


if __name__ == "__main__":
    # Example usage
    user1 = User("Alice")
    user2 = User("Bob")
    group1 = Group("Admins")
    group2 = Group("Editors")
    user1.add_group(group1)
    user1.add_group(group2)
    user2.add_group(group1)
    print(f"User {user1.name} belongs to groups: {[group.name for group in user1.groups]}")
    print(f"User {user2.name} belongs to groups: {[group.name for group in user2.groups]}")

    