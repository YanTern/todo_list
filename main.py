import json, time

with open("tasks.json", "r") as file:
    tasks = json.load(file)


def show_tasks():
    "Показывает задачи в списке"

    for task in tasks:

        task_index = tasks.index(task)

        if task["is_done"] == True:
            print(f"{task_index + 1}. [x] {task['title']}")

        elif task["is_done"] == False:
            print(f"{task_index + 1}. [ ] {task['title']}")

        else:
            print("You have no tasks yet\n")

    print("--------------\n")

def show_completed_tasks():
    "Показывает выполненные задачи"
    completed_tasks = []

    for task in tasks:

        if task["is_done"] == True:
            completed_tasks.append(task)

    if len(completed_tasks) > 0:
        for task in completed_tasks:
            task_index = completed_tasks.index(task)
            print(f"{task_index + 1}. [x] {task['title']}")
    else:
        print(
            "You have no completed tasks\n" 
            "--------------\n"
            )
        
        time.sleep(3)
        show_menu()

    print("--------------\n")

def show_incompleted_tasks():
    "Показывает невыполненные задачи"
    incompleted_tasks = []

    for task in tasks:

        if task["is_done"] == False:
            incompleted_tasks.append(task)

    if len(incompleted_tasks) > 0:
        for task in incompleted_tasks:
            task_index = incompleted_tasks.index(task)
            print(f"{task_index + 1}. [ ] {task['title']}")
    else:
        print(
            "You have no incompleted tasks\n" 
            "--------------\n"
            )
        time.sleep(3)
        show_menu()

def create_task():
    "Создает новую задачу"

    new_task = input("Введите новую задачу: ")
    tasks.append({"title": new_task, "is_done": False})

    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

    print(
        "--------------\n" 
        "A new task has been added" 
        "--------------\n"
        )

def delete_task():
    "Удаляет задачу"

    pass

def complete_task():
    "Отмечает задачу как выполненную"

    pass

def incomplete_task():
    "Отмечает задачу как невыполненную"

    pass

def show_menu():
    print(
        "Welcome to 'To-Do List'\n"
        "\n"
        "Press '1' to show all your tasks\n"
        "Press '2' to show completed tasks\n"
        "Press '3' to show incompleted tasks\n"
        "Press '4' to add a new task\n"
        "Press '5' to exit\n"
    )

    user_choice = int(input("Print your number: "))
    print("--------------\n")

    if user_choice == 1:
        show_tasks()

    elif user_choice == 2:
        show_completed_tasks()

    elif user_choice == 3:
        show_incompleted_tasks()

    elif user_choice == 4:
        create_task()

    elif user_choice == 5:
        print("Goodbye!")


show_menu()
