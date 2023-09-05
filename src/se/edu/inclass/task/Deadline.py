from task.Task import Task 

class Deadline(Task):
    def __init__(self, description):
        super().__init__(description)

    def __str__(self):
        return "(Deadline: " + self.description + ')'
