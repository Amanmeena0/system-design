class Issue:
    def __init__(self):
        self.Project = None
    def set_issue(self, project):
        self.Project = project

class Project:
    def __init__(self):
        self.issues = []
    
    def add_issue(self, issue: Issue):
        self.issues.append(issue)
        issue.set_issue(self)


