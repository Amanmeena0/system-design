class Profile:
    def __init__(self):
        self.user = None

    def set_user(self, user):
        self.user = user


class User:
    def __init__(self):
        self.profile = []

    def add_profile(self, profile: Profile):
        self.profile.append(profile)
        profile.set_user(self)