tasks = []

def view_all_tasks():
    for value in tasks:
        i = tasks.index(value) + 1
        print(f"{i} - {value['title']} - {value['priority']}")

def show_menu():
    print("Press 1 to add task")
    print("Press 2 to delete task")
    print("Press 3 to view all tasks")
    print("Press q to quit")

def add_new_task():
    task_name = input("Enter name of task: ")
    task_priority = input("Enter priority (low/med/high): ")
    # create dictionary
    task = {"title": task_name, "priority": task_priority}
    tasks.append(task)

def delete_task():
    item = int(input("Which item do you want to delete (1, 2, 3, etc) ")) - 1
    del tasks[item]
    
user_input = ""

while user_input != "q":
    show_menu()
    user_input = input("Enter your choice: ")
    if user_input == "1":
        add_new_task()
    if user_input == "2":
        delete_task()
    if user_input == "3":
        view_all_tasks()