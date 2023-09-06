# This class can also be declared as an abstract class, but with modifications to other parts of the code
class Task:
    def __init__(self, description):
        self.description = description

    def get_description(self):
        return self.description
