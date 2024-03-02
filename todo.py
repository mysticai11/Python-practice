def display_menu():
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Exit")

def add_task(tasks, task):
    tasks.append(task)
    print("Task added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks to display.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def mark_task_as_done(tasks, index):
    if 1 <= index <= len(tasks):
        tasks.pop(index - 1)
        print("Task marked as done.")
    else:
        print("Invalid task index.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            task = input("Enter task: ")
            add_task(tasks, task)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            index = int(input("Enter task number to mark as done: "))
            mark_task_as_done(tasks, index)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
