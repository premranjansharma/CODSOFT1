# TO-DO LIST

import json

TODO_FILE = 'todo.json'

def load_todos():
    try:
        with open(TODO_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_todos(todos):
    with open(TODO_FILE, 'w') as file:
        json.dump(todos, file, indent=4)

def add_task(todos):
    task = input("Enter a new task: ")
    todos.append({'task': task, 'status': 'pending'})
    save_todos(todos)
    print("Task added successfully!")

def view_tasks(todos):
    if not todos:
        print("No tasks found.")
    else:
        print("To-Do List:")
        for idx, todo in enumerate(todos, start=1):
            print(f"{idx}. {todo['task']} - {todo['status']}")

def update_task(todos):
    view_tasks(todos)
    try:
        task_num = int(input("Enter the task number to update: "))
        if 1 <= task_num <= len(todos):
            task = todos[task_num - 1]
            new_task = input(f"Enter new task description (current: {task['task']}): ") or task['task']
            new_status = input(f"Enter new status (pending/completed) (current: {task['status']}): ").lower() or task['status']
            if new_status not in ['pending', 'completed']:
                print("Invalid status. Please enter 'pending' or 'completed'.")
                return
            task['task'] = new_task
            task['status'] = new_status
            save_todos(todos)
            print("Task updated successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_task(todos):
    view_tasks(todos)
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(todos):
            todos.pop(task_num - 1)
            save_todos(todos)
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    todos = load_todos()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_task(todos)
        elif choice == '2':
            view_tasks(todos)
        elif choice == '3':
            update_task(todos)
        elif choice == '4':
            delete_task(todos)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
