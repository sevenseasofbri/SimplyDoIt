# Data Manager class to handle data read and write
import os
import io
from typing import List
from task.Deadline import Deadline
from task.Task import Task
from task.Event import Event
from task.Todo import Todo

class DataManager:
    def __init__(self, file_name):
        self.data_file = file_name

    # Returns the data file name
    def get_data_file(self):
        return self.data_file

    # Creates the data file if it does not exist
    def create_file(self):
        try:
            if os.path.exists(self.data_file):
                print("file exists")
                return

            if not os.path.exists(os.path.dirname(self.data_file)):
                os.makedirs(os.path.dirname(self.data_file))

            open(self.data_file, 'w').close()
        except IOError as e:
            print("Cannot create file; reason: " + str(e))

    # Reads data from the data file
    def read_file(self):
        try:
            if not os.path.exists(self.data_file):
                raise FileNotFoundError

            with open(self.data_file, 'r') as file:
                data_items = file.readlines()

            if not data_items:
                print("empty file")
                raise IOError

            return data_items
        except (FileNotFoundError, IOError) as e:
            print("File access issues. Please check")
            return []

    # Loads data from the data file
    def load_data(self):
        task_list = None
        try:
            data_items = self.read_file()
            task_list = self.parse(data_items)
        except IOError:
            print("File access issues. Please check")
        return task_list

    # Parses the data read from the data file
    def parse(self, data_items):
        all_tasks = []
        for line in data_items:
            task_type = self.get_task_type(line)
            task_description = self.get_task_description(line)
            task_completion = self.get_task_completion(line)
            if task_type == "T":
                todo = Todo(task_description, task_completion)
                all_tasks.append(todo)
            elif task_type == "D":
                deadline_description, due_date = self.get_deadline_details(task_description)
                deadline = Deadline(deadline_description, due_date, task_completion)
                all_tasks.append(deadline)
            elif task_type == "E":
                event_description, start_time, end_time = self.get_event_details(task_description)
                event = Event(event_description, start_time, end_time, task_completion)
                all_tasks.append(event)
            else:
                print("Unknown task encountered. Skipping")
        return all_tasks
    
    # Parses deadline details and returns the deadline description and due date
    def get_deadline_details(self, task_description):
        parts = task_description.split(",")
        if len(parts) != 3:
            print("Error: Invalid deadline format. Populating with empty values...")
            return None, None
        # Extract deadline description and due date
        due_date = parts[0].strip()
        deadline_description = parts[1].strip()
        return deadline_description, due_date

    # Parses the event details and returns the event description, start time and end time
    def get_event_details(self, task_description):
        parts = task_description.split(",")
        if len(parts) != 3:
            print("Error: Invalid event format. Populating with empty values...")
            return None, None, None
        # Extract time/date part and event description
        time_date_part = parts[0].strip()
        event_description = parts[1].strip()
        time_parts = time_date_part.split("-")
        if len(time_parts) != 2:
            print("Error: Invalid date/time format. Populating with empty values...")
            return event_description, None, None
        # Extract start and end time
        start_time = time_parts[0].strip()
        end_time = time_parts[1].strip()
        return event_description, start_time, end_time
    
    @staticmethod
    def get_task_description(line):
        start_index = line.find(',')
        task_description = line[start_index+1:].strip()
        return task_description

    @staticmethod
    def get_task_type(line):
        task_type = line[0:2].replace("[", "").replace("]", "")
        return task_type

    @staticmethod
    def get_task_completion(line):
        start_index = line.rfind(',')
        task_completion = line[start_index+1:].strip()
        return "Task Completed" if task_completion == "[X]" else "Task Not Completed"

    @staticmethod
    def get_taskcompletion(line):
        # Deprecated, please use get_task_completion instead
        return DataManager.get_task_completion(line)
