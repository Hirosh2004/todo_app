# todo_app.py

FILE_NAME = "tasks.txt"

def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        # Create the file if it doesn't exist
        with open(FILE_NAME, "w") as file:
            return []


# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Menu display
def show_menu():
    print("\nTo-Do List")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

# Main app
tasks = load_tasks()

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == '1':
        if tasks:
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task}")
        else:
            print("No tasks yet!")

    elif choice == '2':
        new_task = input("Enter the task: ")
        tasks.append(new_task)
        save_tasks(tasks)
        print("Task added.")

    elif choice == '3':
        task_num = int(input("Enter task number to remove: "))
        if 0 < task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Removed: {removed}")
        else:
            print("Invalid task number.")

    elif choice == '4':
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
