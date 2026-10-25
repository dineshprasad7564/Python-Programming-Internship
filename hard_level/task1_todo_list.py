"""
Hard Level - Task 1: Command Line To-Do List Application
Objective: Build a complete menu-driven task manager.

Users can add, view, and delete tasks. Tasks are stored in a
list during the session and saved to tasks.json so they
survive even after the program is closed.
"""

import json
import os

TASKS_FILE = "tasks.json"


def load_tasks():
    """Load previously saved tasks, or return an empty list on first run."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    """Save the current task list to disk."""
    with open(TASKS_FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)


def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet. Add one first!")
        return
    print("\n===== YOUR TASKS =====")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def add_task(tasks):
    task = input("Enter the task description: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print(f"Task added: '{task}'")
    else:
        print("Task cannot be empty!")


def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        number = int(input("Enter the task number to delete: "))
        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            save_tasks(tasks)
            print(f"Task deleted: '{removed}'")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")


def main():
    tasks = load_tasks()

    while True:
        print("\n===== TO-DO LIST =====")
        print("1. Add a task")
        print("2. View all tasks")
        print("3. Delete a task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Goodbye! Your tasks have been saved.")
            break
        else:
            print("Invalid choice! Please select 1, 2, 3, or 4.")


main()
