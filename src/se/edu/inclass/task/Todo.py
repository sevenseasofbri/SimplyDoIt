from task.Task import Task 

class Todo(Task):
    def __init__(self, description, completion):
        super().__init__(description, completion)

    def __str__(self):
        return "{Todo: " + self.description + ' - ' +  self.completion + '}'
