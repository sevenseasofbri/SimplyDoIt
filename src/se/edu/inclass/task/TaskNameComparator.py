from typing import List
from task.Task import Task 

class TaskNameComparator:
    @staticmethod
    def compare(t1: Task, t2: Task) -> int:
        return str(t1.get_description()).lower().compare(str(t2.get_description()).lower())


