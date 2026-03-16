
from task import Task


def parse_tasks(file_path):
    tasks = []
    with open(file_path, 'r') as file:
        start = False
        for line in file:
            if line.strip() == "*":
                task = Task("None", "None", "None")  # Initialize a new Task object
                counter = 0
            elif start:
                if counter == 0:
                    task.name = line.strip()
                elif counter == 1:
                    task.category = line.strip()
                elif counter == 2:
                    task.start = line.strip()
                counter += 1
    return tasks

# Example in file:
# *
# Task Name
# Task Category
# Task Start
# *

def save_tasks(tasks, file_path):
    with open(file_path, 'w') as file:
        for task in tasks:
            file.write("*\n")
            file.write(f"{task.name}\n")
            file.write(f"{task.category}\n")
            file.write(f"{task.start}\n")

def add_task(tasks, name, category, start):
    task = Task(name)
    task.category = category
    task.start = start
    tasks.append(task)

def add_task_user(tasks):
    name = input("Enter task name: ")
    category = input("Enter task category: ")
    start = input("Enter task start date: ")
    add_task(tasks, name, category, start)

def print_tasks(tasks):
    for task in tasks:
        print(f"Name: {task.name}, Category: {task.category}, Start: {task.start}")

def CLEAR_FILE(file_path):
    with open(file_path, 'w') as file:
        file.write("")