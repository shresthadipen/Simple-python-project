class ToDoList:
    def __init__(self):
        self.tasks = []

    def show_tasks(self):
        if len(self.tasks) == 0:
            print("No tasks to display!")
        else:
            i = 1
        for task in self.tasks:
            print(f"{i}. {task}")
            i += 1


    def add_task(self):
        task = input("Enter the new task: ")
        self.tasks.append(task)
        print(f"Task '{task}' added.")

    def delete_task(self):
        if len(self.tasks) == 0:
            print("No tasks to delete!")
        else:
            try:
                task_number = int(input("Enter the task number to delete: "))
                if 0 < task_number <= len(self.tasks):
                    removed_task = self.tasks.pop(task_number - 1)
                    print(f"Task '{removed_task}' removed.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")


to_do_list = ToDoList()
choice = 0

while choice != '4':
    print("\n1. View Tasks\n2. Add Task\n3. Delete Task\n4. Exit")
    choice = input("Choose an option(from 1-4): ")

    if choice == '1':
        to_do_list.show_tasks()
    elif choice == '2':
        to_do_list.add_task()
    elif choice == '3':
        to_do_list.delete_task()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Try again.")
