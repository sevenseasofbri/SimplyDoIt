from task.Task import Task 

class Deadline(Task):
    def __init__(self, description, completion):
        super().__init__(description, completion)

    def __str__(self):
        return "(Deadline: " + self.description + ' - ' + self.completion + ')'
