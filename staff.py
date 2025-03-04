from user import User

class Staff(User):
    def __init__(self,
                 full_name,
                 userID,
                 password,
                 phone,
                 email):
        
        super().__init__(full_name, userID, password, phone, email, role='staff')
        self.tasks = []
        self.reports = []

    def add_task(self, task):
        self.tasks.append(task)

    def add_report(self, report):
        self.reports.append(report)

    def get_tasks(self):
        return self.tasks

    def get_reports(self):
        return self.reports