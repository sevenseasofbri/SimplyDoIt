from task.Task import Task 

class Event(Task):
    def __init__(self, description):
        super().__init__(description)

    def __str__(self):
        return "[Event: " + self.description + ']'
