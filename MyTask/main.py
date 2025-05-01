tasks=[]

def show_menu():
    print("=== To-Do Task Manager ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter the task: ")
    tasks.append({"task": task, "completed": False})
    print(f"Task '{task}' added.")

def view_tasks():
    if not tasks:
        print("No tasks available.")
        return
    print("=== Tasks ===")
    for i, task in enumerate(tasks, start=1):
        status = "✔️" if task["completed"] else "❌"
        print(f"{i}. {task['task']} [{status}]")

def mark_task_completed():
    view_tasks()
    if not tasks:
        return
    try:
        task_number = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= task_number < len(tasks):
            tasks[task_number]["completed"] = True
            print(f"Task '{tasks[task_number]['task']}' marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    if not tasks:
        return
    try:
        task_number = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_number < len(tasks):
            deleted_task = tasks.pop(task_number)
            print(f"Task '{deleted_task['task']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    show_menu()
    choice = input("Choose an option (1-5): ")
    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        mark_task_completed()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Exiting the task manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
# This is a simple command-line To-Do Task Manager in Python.