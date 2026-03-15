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

        print("\n--------------\n" "\nAll my tasks:\n")

        if len(tasks) > 0:

            for i, task in enumerate(tasks, start=1):

                if task["is_done"] == True:
                    print(f"{i}. [x] {task['title']}")

                elif task["is_done"] == False:
                    print(f"{i}. [ ] {task['title']}")

            print("\n--------------\n")

            print(
                "'task number' - choose the task\n"
                "'menu' - main menu\n"
                "'del' - delete all your tasks\n"
                "'v' - mark all your tasks as 'complete'\n"
                "'x' - mark all your tasks as 'incomplete'\n"
                "'add' - add a new task\n"
            )

        else:
            print("You have no tasks yet\n")

            print("\n--------------\n")

            print("'menu' - main menu\n" "'add' - add a new task\n")

        user_choice = input("Print your command: ").strip().lower()

        if user_choice.isdigit():

            num = int(user_choice.strip())

            if 1 <= num <= len(tasks):
                show_task_menu(tasks, num - 1)

            else:
                print(
                    "\n--------------\n"
                    "There's no task task with this number"
                    "\n--------------\n"
                )
                time.sleep(2)
                show_tasks()

        else:

            match user_choice:

                case "menu":
                    print("\n--------------\n")
                    main()

                case "add":
                    create_task()

                case "v":

                    for task in tasks:
                        task["is_done"] = True

                    with open("tasks.json", "w", encoding="utf-8") as file:
                        json.dump(tasks, file, ensure_ascii=False, indent=4)

                    print(
                        "\n--------------\n"
                        "All tasks have been completed"
                        "\n--------------\n"
                    )
                    time.sleep(2)
                    show_tasks()

                case "x":

                    for task in tasks:
                        task["is_done"] = False

                    with open("tasks.json", "w", encoding="utf-8") as file:
                        json.dump(tasks, file, ensure_ascii=False, indent=4)

                    print(
                        "\n--------------\n"
                        "All tasks have been incompleted"
                        "\n--------------\n"
                    )
                    time.sleep(2)
                    show_tasks()

                case "del":
                    print(
                        "\n--------------\n"
                        "\nAre you sure?\n"
                        "'1' - Yes\n"
                        "'2' - No"
                        "\n--------------\n"
                    )

                    sub_choice = input("Print your command: ").strip().lower()

                    if sub_choice == "1":
                        tasks.clear()

                        with open("tasks.json", "w", encoding="utf-8") as file:
                            json.dump(tasks, file, ensure_ascii=False, indent=4)

                        print(
                            "\n--------------\n"
                            "All tasks have been deleted"
                            "\n--------------\n"
                        )
                        time.sleep(2)
                        main()

                    elif sub_choice == "2":
                        show_tasks()

                    elif sub_choice == "":
                        print("\n--------------\n" "Try again" "\n--------------\n")
                        time.sleep(1)
                        show_tasks()

                case "":
                    print("\n--------------\n" "Try again" "\n--------------\n")
                    time.sleep(2)
                    show_tasks()

                case _:
                    print("\n--------------\n" "Try again" "\n--------------\n")
                    time.sleep(2)
                    show_tasks()

    def show_task_menu(tasks, index):
        "Открывает подменю выбранной задачи"

        task = tasks[index]

        if task["is_done"] == True:
            print(f"[x] {task['title']}")

        else:
            print(f"[ ] {task['title']}")

        print(
            "\n--------------\n"
            "\nPress '1' to rename the task\n"
            "Press '2' to delete the task\n"
            "Press '3' to change complete status of the task\n"
            "Press '4' to return\n"
        )

        user_choice = input("Print your number: ").strip().lower()

        match user_choice:

            case "1":
                rename_task(index)
                time.sleep(2)
                show_tasks()

            case "2":
                delete_task(index)
                time.sleep(2)
                show_tasks()

            case "3":
                change_complete_status(index)
                time.sleep(2)
                show_tasks()

            case "4":
                show_tasks()

            case "":
                print("\n--------------\n" "Try again" "\n--------------\n")
                time.sleep(2)
                show_task_menu(tasks, index)

    def show_completed_tasks():
        "Показывает выполненные задачи"

        if len(completed_tasks) > 0:
            print("\nCompleted tasks:\n")

            for i, task in enumerate(completed_tasks, start=1):
                print(f"{i}. [x] {task['title']}")
        else:
            print("\nYou have no completed tasks\n" "\n--------------\n")

            time.sleep(2)
            main()

        print("\n--------------\n")

        print(
            "'task number' - choose the task\n"
            "'menu' - main menu\n"
            "'del' - delete all completed tasks\n"
            "'x' - mark all your tasks as 'incomplete'\n"
            "'add' - add a new task\n"
        )

        user_choice = input("Print your command: ").strip().lower()

        if user_choice.isdigit():

            if 1 <= int(user_choice) <= len(completed_tasks):
                print("sth")

            else:
                print(
                    "\n--------------\n"
                    "There's no task task with this number"
                    "\n--------------\n"
                )
                time.sleep(2)
                show_completed_tasks()

        else:

            match user_choice:

                case "menu":
                    print("\n--------------\n")
                    main()

                case "add":
                    create_task()

                case "del":
                    tasks[:] = [task for task in tasks if not task["is_done"]]

                    with open("tasks.json", "w", encoding="utf-8") as file:
                        json.dump(tasks, file, ensure_ascii=False, indent=4)

                    print(
                        "\n--------------\n"
                        "All completed tasks have been deleted"
                        "\n--------------\n"
                    )
                    time.sleep(2)
                    main()

                case "x":
                    for task in tasks:
                        task["is_done"] = False

                    with open("tasks.json", "w", encoding="utf-8") as file:
                        json.dump(tasks, file, ensure_ascii=False, indent=4)

                    print(
                        "\n--------------\n"
                        "Status has been changed"
                        "\n--------------\n"
                    )
                    time.sleep(2)
                    main()

                case "":
                    print("\n--------------\n" "Try again" "\n--------------\n")
                    time.sleep(2)
                    show_completed_tasks()

                case _:
                    print("\n--------------\n" "Try again" "\n--------------\n")
                    time.sleep(2)
                    show_completed_tasks()

        print("\n--------------\n")

    def show_incompleted_tasks():
        "Показывает невыполненные задачи"

        if len(incompleted_tasks) > 0:
            print("\nIncompleted tasks:\n")

            for i, task in enumerate(incompleted_tasks, start=1):
                print(f"{i}. [ ] {task['title']}")
        else:
            print("You have no incompleted tasks\n" "\n--------------\n")
            time.sleep(2)
            main()

        print("\n--------------\n")

        print(
            "'task number' - choose the task\n"
            "'0' - main menu\n"
            "'del' - delete all incompleted tasks\n"
            "'v' - mark all your tasks as 'complete'\n"
            "'add' - add a new task\n"
        )

        user_choice = input("Print your command: ").strip().lower()

        match user_choice:

            case "0":
                print("\n--------------\n")
                main()

            case "add":
                create_task()

            case "v":
                for task in tasks:
                    task["is_done"] = True

                with open("tasks.json", "w", encoding="utf-8") as file:
                    json.dump(tasks, file, ensure_ascii=False, indent=4)

                print(
                    "\n--------------\n" "Status has been changed" "\n--------------\n"
                )
                time.sleep(2)
                main()

            case "del":
                tasks[:] = [task for task in tasks if task["is_done"]]

                with open("tasks.json", "w", encoding="utf-8") as file:
                    json.dump(tasks, file, ensure_ascii=False, indent=4)

                print(
                    "\n--------------\n"
                    "All incompleted tasks have been deleted"
                    "\n--------------\n"
                )
                time.sleep(2)
                main()

            case "":
                print("\n--------------\n" "Try again" "\n--------------\n")
                time.sleep(2)
                show_incompleted_tasks()

            case _:
                print("\n--------------\n" "Try again" "\n--------------\n")
                time.sleep(2)
                show_incompleted_tasks()

    def create_task():
        "Создает новую задачу"

        print("\n--------------\n")

        new_task = input("Print your new task: ").strip()

        if new_task != "":
            tasks.append({"title": new_task, "is_done": False})

            with open("tasks.json", "w") as file:
                json.dump(tasks, file, indent=4)

        else:
            print("\n--------------\n" "Try again" "\n--------------\n")
            time.sleep(2)
            create_task()

        print("\n--------------\n" "\nA new task has been added\n" "\n--------------\n")

        time.sleep(2)
        show_tasks()

    def rename_task(index):
        "Переименовывает задачу"

        print("\n--------------\n")
        new_name = input("Print a new name: ").strip()

        if new_name != "":
            tasks[index]["title"] = new_name

            with open("tasks.json", "w", encoding="utf-8") as file:
                json.dump(tasks, file, ensure_ascii=False, indent=4)

        else:

            print("\n--------------\n" "Try again" "\n--------------\n")
            time.sleep(2)
            rename_task(index)

        print("\n--------------\n" "The name has been changed" "\n--------------\n")

    def delete_task(index):
        "Удаляет задачу"

        print(
            "\n--------------\n"
            "\nAre you sure?\n"
            "\n'1' - Yes\n"
            "'2' - No\n"
            "\n--------------\n"
        )

        sub_choice = input("Print your command: ").strip().lower()

        if sub_choice == "1":

            del tasks[index]
            print("\n--------------\n" "The task has been deleted" "\n--------------\n")

            with open("tasks.json", "w", encoding="utf-8") as file:
                json.dump(tasks, file, ensure_ascii=False, indent=4)

        elif sub_choice == "2":
            show_tasks()

        else:
            print("Try again")
            time.sleep(2)
            delete_task(task)

    def change_complete_status(index):
        "Отмечает задачу как выполненную / невыполненную"

        if tasks[index]["is_done"] == True:
            tasks[index]["is_done"] = False

        elif tasks[index]["is_done"] == False:
            tasks[index]["is_done"] = True

        with open("tasks.json", "w", encoding="utf-8") as file:
            json.dump(tasks, file, ensure_ascii=False, indent=4)

        print("\n--------------\n" "Status has been changed" "\n--------------\n")

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

        user_choice = input("Print your number: ").strip().lower()

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
                print("\n--------------\n" "\nGoodbye!\n")
                return

            case "":
                print("Try again" "\n--------------\n")
                time.sleep(2)
                main()

            case _:
                print("Try again" "\n--------------\n")
                time.sleep(2)
                main()

    show_menu()


main()
