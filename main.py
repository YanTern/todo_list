import json, time

with open("tasks.json", "r") as file:
    tasks = json.load(file)

def main():
    completed_tasks = []
    incompleted_tasks = []

    for task in tasks:

        if task["is_done"] == True:
            completed_tasks.append(task)

        elif task["is_done"] == False:
            incompleted_tasks.append(task)


    def show_tasks():
        "Показывает задачи в списке"

        print(
            "\n--------------\n"
            "\nAll my tasks:\n"
            )

        if len(tasks) > 0:

            for task in tasks:
                task_index = tasks.index(task)

                if task["is_done"] == True:
                    print(f"{task_index + 1}. [x] {task['title']}")

                elif task["is_done"] == False:
                    print(f"{task_index + 1}. [ ] {task['title']}")

            print("\n--------------\n")

            print(
                "'task number' - choose the task\n"
                "'0' - main menu\n"
                "'del' - delete all your tasks\n"
                "'v' - mark all your tasks as 'complete'\n"
                "'x' - mark all your tasks as 'incomplete'\n"
                "'add' - add a new task\n"
                )

        else:
            print("You have no tasks yet\n")

            print("\n--------------\n")

            print(
                "'0' - main menu\n"
                "'add' - add a new task\n"
                )

        user_choice = input("Print your command: ")

        match user_choice:
        
            case "0":
                print("\n--------------\n")
                main()

            case "add":
                create_task()

            case "del":
                print(
                    "\n--------------\n"
                    "\nAre you sure?\n"
                    "\n'1' - Yes\n"
                    "\n'2' - No\n"
                    "\n--------------\n"
                    )
            
                sub_choice = input("Print your command: ")

                if sub_choice == "1":
                    tasks.clear()
                    print(
                        "\n--------------\n"
                        "\nAll tasks have been deleted\n"
                        "\n--------------\n"
                    )
                    time.sleep(2)
                    main()

                elif sub_choice == "2":
                    show_tasks()
            
            case _:
                print(
                    "\n--------------\n" 
                    "Try again" 
                    "\n--------------\n"
                    )
                time.sleep(1)
                show_tasks()


    def show_completed_tasks():
        "Показывает выполненные задачи"

        if len(completed_tasks) > 0:
            print("\nCompleted tasks:\n")

            for task in completed_tasks:
                task_index = completed_tasks.index(task)
                print(f"{task_index + 1}. [x] {task['title']}")
        else:
            print(
                "\nYou have no completed tasks\n" 
                "\n--------------\n"
                )

            time.sleep(3)
            main()

        print(
            "'task number' - choose the task\n"
            "'0' - main menu\n"
            "'del' - delete all completed tasks\n"
            "'x' - mark all your tasks as 'incomplete'\n"
            "'add' - add a new task\n"
        )

        user_choice = input("Print your command: ")

        match user_choice:

            case "0":
                print("\n--------------\n")
                main()

            case "add":
                create_task()

            case _:
                print(
                    "\n--------------\n" 
                    "Try again" 
                    "\n--------------\n"
                    )
                time.sleep(1)
                show_completed_tasks()

        print("\n--------------\n")


    def show_incompleted_tasks():
        "Показывает невыполненные задачи"

        if len(incompleted_tasks) > 0:
            print("\nIncompleted tasks:\n")

            for task in incompleted_tasks:
                task_index = incompleted_tasks.index(task)
                print(f"{task_index + 1}. [ ] {task['title']}")
        else:
            print(
                "You have no incompleted tasks\n" 
                "\n--------------\n"
                )
            time.sleep(3)
            main()

        print("\n--------------\n")

        print(
            "'task number' - choose the task\n"
            "'0' - main menu\n"
            "'del' - delete all incompleted tasks\n"
            "'x' - mark all your tasks as 'complete'\n"
            "'add' - add a new task\n"
        )

        user_choice = input("Print your command: ")

        match user_choice:
            
            case "0":
                print("\n--------------\n")
                main()

            case "add":
                create_task()

            case _:
                print(
                    "\n--------------\n" 
                    "Try again" 
                    "\n--------------\n"
                    )
                time.sleep(1)
                show_incompleted_tasks()


    def create_task():
        "Создает новую задачу"

        print("\n--------------\n")

        new_task = input("Введите новую задачу: ")
        tasks.append({"title": new_task, "is_done": False})

        with open("tasks.json", "w") as file:
            json.dump(tasks, file, indent=4)

        print(
            "\n--------------\n" 
            "\nA new task has been added\n" 
            "\n--------------\n"
            )

        time.sleep(2)
        show_tasks()


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

        user_choice = input("Print your number: ")

        print("\n--------------\n")

        match user_choice:

            case "1":
                show_tasks()

            case "2":
                show_completed_tasks()

            case "3":
                show_incompleted_tasks()

            case "4":
                create_task()

            case "5":
                print(
                    "\n--------------\n"
                    "\nGoodbye!\n"
                    )
                return

            case _:
                print(
                    "Try again" 
                    "\n--------------\n"
                    )
                time.sleep(1)
                main()


    show_menu()

main()