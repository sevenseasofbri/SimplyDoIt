class Task:
    def __init__(self, description, completion):
        self.description = description
        self.completion = completion

    def get_description(self):
        return self.description
    
    def get_status(self):
        return self.completion
