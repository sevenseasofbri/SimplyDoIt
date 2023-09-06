from task.Task import Task 

class Event(Task):
    def __init__(self, description, completion):
        super().__init__(description, completion)

    def __str__(self):
        return "[Event: " + self.description + ' - ' + self.completion + ']'
