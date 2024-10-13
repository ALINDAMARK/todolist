from asyncio import tasks

def key():
    tasks = []  # Initialize tasks as an empty list
    
    while True:
        print("\n==== TO DO LIST ====")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Tasks as Done")
        print("4. Exit\n")

        choice = input("Enter your choice: ")

        if choice == '1':
            n_tasks = int(input("How many tasks do you want to add?: "))
            
            if n_tasks > 0:
                tasks.extend([{"task": input(f"Enter task {i+1}: "), "done": False} for i in range(n_tasks)])
                print("\nTasks added!")
            else:
                print("\nNo tasks were added.")

        elif choice == '2':
            if tasks:
                for index, task in enumerate(tasks, start=1):
                    status = "Done" if task["done"] else "Not Done"
                    print(f"{index}. {task['task']} - {status}")
            else:
                print("\nNo tasks available.")

        elif choice == '3':
            if tasks:
                task_index = int(input("Enter the task number you want to mark as done: ")) - 1
                if 0 <= task_index < len(tasks):
                    tasks[task_index]["done"] = True
                    print("\nTask marked as done!")
                else:
                    print("\nInvalid task number.")
            else:
                print("\nNo tasks available.")

        elif choice == '4':
            print("\nExiting the To Do List.")
            break

        else:
            print("\nInvalid choice. Please try again.")

# Run the function
key()