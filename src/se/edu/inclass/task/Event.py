from task.Task import Task 

class Event(Task):
    def __init__(self, description, start_time, end_time, completion):
        super().__init__(description, completion)
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return "[Event: " + self.description + f", Start Time: {self.start_time}, End Time: {self.end_time}" + ' - ' + self.completion + ']'
