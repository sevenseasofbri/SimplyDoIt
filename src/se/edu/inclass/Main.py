from data.DataManager import DataManager
from task.Deadline import Deadline
from task.Task import Task
from task.TaskNameComparator import TaskNameComparator
from typing import List

def main():
    print("Welcome to Task (stream) manager\n")
    dm = DataManager("./data/data.txt")
    tasks_data = dm.load_data()

    # Print data
    print()
    print("Printing deadlines before sorting")
    print_deadlines(tasks_data)

    # Count deadlines
    print("Total number of deadlines:", count_deadlines(tasks_data))

    # Print deadlines using streams
    print("Printing deadlines after sorting")
    print_deadlines_using_stream(tasks_data)

    # Count deadlines using streams
    print("Total number of deadlines counted using streams:", count_deadlines_using_stream(tasks_data))

    # Filter tasks using streams
    filtered_list = filter_task_list_using_streams(tasks_data, "11")
    print("\nFiltered list of tasks:")
    print_data(filtered_list)

def count_deadlines(tasks_data: List[Task]) -> int:
    count = 0
    for task in tasks_data:
        if isinstance(task, Deadline):
            count += 1
    return count

def count_deadlines_using_stream(tasks: List[Task]) -> int:
    count = sum(1 for task in tasks if isinstance(task, Deadline))
    return count

def print_data(tasks_data: List[Task]):
    print("Printing data using iteration")
    for task in tasks_data:
        print(task)

def print_deadlines(tasks_data: List[Task]):
    print("Printing deadline using iteration")
    for task in tasks_data:
        if isinstance(task, Deadline):
            print(task)

def print_deadlines_using_stream(tasks: List[Task]):
    print("Printing deadline using streams")
    sorted_tasks = sorted(tasks, key=lambda x: x.get_description().lower())
    for task in filter(lambda x: isinstance(x, Deadline), sorted_tasks):
        print(task)

def filter_task_list_using_streams(tasks: List[Task], filter_string: str) -> List[Task]:
    filtered_list = [task for task in tasks if filter_string in task.get_description()]
    return filtered_list

if __name__ == "__main__":
    main()
