import json

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
            print("You have no tasks yet")


def create_task():
    "Создает новую задачу"

    new_task = input("Введите новую задачу: ")
    tasks.append({"title": new_task, "is_done": False})

    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)


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
        "Welcome to 'To-Do List' \n",
        "Press '1' to show all your tasks \n",
        "Press '2' to show complete tasks \n",
        "Press '3' to show incomplete tasks \n",
        "Press '4' to exit",
    )

    user_inp = int(input("Print your number: "))

    if user_inp == 1:
        show_tasks()

    if user_inp == 4:
        print("Goodbye!")


show_menu()
