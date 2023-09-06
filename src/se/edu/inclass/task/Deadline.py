from task.Task import Task 

class Deadline(Task):
    def __init__(self, description, due_date):
        super().__init__(description)
        self.due_date = due_date

    def __str__(self):
        return "(Deadline: " + self.description + ', Due Date: ' + str(self.due_date) + ')'
