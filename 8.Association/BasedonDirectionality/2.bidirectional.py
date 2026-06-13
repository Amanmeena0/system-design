class Team:
    def __init__(self):
        self.team = None

    def set_team(self, team):
        self.team = team


class Developer:
    def __init__(self):
        self.developer = []
    
    def add_developer(self, dev:Developer):
        self.developer.append(dev)
        dev.set_team(self)