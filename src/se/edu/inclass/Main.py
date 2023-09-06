# Main.py is the entry point of the program
from data.DataManager import DataManager
from task.Deadline import Deadline
from task.Task import Task
from typing import List

# Main function
def main():
    print("------------------------------------------------------------")
    print("Welcome to SimplyDoIt\n")
    dm = DataManager("./data/data.txt")
    tasks_data = dm.load_data()

    # Print data
    print("------------------------------------------------------------")
    print("Deadlines in the task list:")
    print_deadlines(tasks_data)

    # Count deadlines using streams
    print("\n")
    print("Total number of deadlines counted using streams:", count_deadlines_using_stream(tasks_data))

    # Filter tasks using streams
    filtered_list = filter_task_list_using_streams(tasks_data, "Meeting")
    print("\nFiltered list of tasks (filtered by keyword \"Meeting\"):")
    print_data(filtered_list)
    print("------------------------------------------------------------")

    # Filter task status using streams
    filtered_list = filter_task_list_status_using_streams(tasks_data, "Task Not Completed")
    print("\nFiltered list of tasks (filtered by \"Task Not Completed\" status):")
    print_data(filtered_list)
    print("------------------------------------------------------------")

# Counts total deadlines using streams
def count_deadlines_using_stream(tasks: List[Task]) -> int:
    count = sum(1 for task in tasks if isinstance(task, Deadline))
    return count

# Prints data using iteration
def print_data(tasks_data: List[Task]):
    print("     Printing data using iteration")
    for task in tasks_data:
        print(task)

# Prints deadlines using iteration
def print_deadlines(tasks_data: List[Task]):
    print("     Printing deadline using iteration")
    for task in tasks_data:
        if isinstance(task, Deadline):
            print(task)

# Filters tasks using streams
def filter_task_list_using_streams(tasks: List[Task], filter_string: str) -> List[Task]:
    filtered_list = [task for task in tasks if filter_string in task.get_description()]
    return filtered_list

# Filters tasks by completion status using streams
def filter_task_list_status_using_streams(tasks: List[Task], completion_status: str) -> List[Task]:
    filtered_list = [task for task in tasks if task.get_status() == completion_status]
    return filtered_list


if __name__ == "__main__":
    main()
