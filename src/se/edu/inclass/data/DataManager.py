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
            if task_type == "T":
                todo = Todo(task_description)
                all_tasks.append(todo)
            elif task_type == "D":
                deadline_description, due_date = self.get_deadline_details(task_description)
                deadline = Deadline(deadline_description, due_date)
                all_tasks.append(deadline)
            elif task_type == "E":
                event = Event(task_description)
                all_tasks.append(event)
            else:
                print("Unknown task encountered. Skipping")
        return all_tasks
    
    # Parses deadline details and returns the deadline description and due date
    def get_deadline_details(self, task_description):
        parts = task_description.split(",")
        if len(parts) != 2:
            print("Error: Invalid deadline details. Populating with empty values...")
            return None, None
        # Extract deadline description and due date
        due_date = parts[0].strip()
        deadline_description = parts[1].strip()
        return deadline_description, due_date

    @staticmethod
    def get_task_description(line):
        task_description = line[4:].strip()
        return task_description

    @staticmethod
    def get_task_type(line):
        task_type = line[0:2].replace("[", "").replace("]", "")
        return task_type
