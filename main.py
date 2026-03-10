import json

with open("tasks.json", "r") as file:
    tasks = json.load(file)


def show_tasks():
    "Показывает задачи в списке"

    pass


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


def complete_task():
    "Отмечает задачу как невыполненную"

    pass


create_task()
