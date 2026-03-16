"""
main.py

Entry point for the application.
"""

import sys
from task import Task
import src

def setup():
    """
    Perform initial setup tasks.
    Example:
        - Load configuration
        - Initialize resources
        - Setup logging
    """
    pass


def run():
    """
    Main program logic.
    """
    pass


def cleanup():
    """
    Cleanup resources before exiting.
    Example:
        - Close files
        - Disconnect services
        - Save state
    """
    pass


def main():
    """
    Main function controlling program flow.
    """
    try:
        setup()
        run()
    except Exception as e:
        print(f"Error occurred: {e}", file=sys.stderr)
        sys.exit(1)
    finally:
        cleanup()


if __name__ == "__main__":
    #main()
    tasks = src.parse_tasks("resources/tasks.txt")
    
    src.add_task(tasks, "change oil", "Car", "03/17/26")
    while True:
        src.add_task_user(tasks)
        cont = input("Do you want to add another task? (yes/no): ")
        if cont.lower() != "yes":
            break

    src.print_tasks(tasks)
    src.save_tasks(tasks, "resources/tasks.txt")
    src.save_tasks(tasks, "resources/backup.txt")
    #src.CLEAR_FILE("resources/tasks.txt")

