
tasks = []  


def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Quit")


def add_task(tasks_list):
    task = input("Please nter a task: ").strip()
    if task:
        tasks_list.append(task)
        print("Task added!")
    else:
        print("Can't have empty tasks.")


def view_tasks(tasks_list):
    if not tasks_list:
        print("No tasks here!")
    else:
        print("Your tasks:")
        for i, task in enumerate(tasks_list, start=1):
            print(f"{i}. {task}")


def delete_task(tasks_list):
    if not tasks_list:
        print("Nothing here to delete")
        return

    try:
        task_num = int(input("Which task number to delete? "))
        if 1 <= task_num <= len(tasks_list):
            deleted = tasks_list.pop(task_num - 1)
            print(f"Deleted: {deleted}")
        else:
            print("That task number doesn’t exist.")
    except ValueError:
        print("Enter a number for the task, not a word!")


def main():
    while True:
        show_menu()
        try:
            choice = int(input("Choose a menu option (1-4): "))

            if choice == 1:
                add_task(tasks)
            elif choice == 2:
                view_tasks(tasks)
            elif choice == 3:
                delete_task(tasks)
            elif choice == 4:
                print("Bye!")
                break
            else:
                print("That is not an option. Please try again")
        except ValueError:
            print("Invalid. Enter numbers only")
        except Exception as e:
            print(f"Oops! Something went wrong: {e}")
        finally:
            print("Back to the main menu...")


if __name__ == "__main__":
    main()


















































# tasks = []



# tasks = [] 

# def show_menu():
#     print("\n--- To-Do List Menu ---")
#     print("1. Add Task")
#     print("2. View Tasks")
#     print("3. Delete Task")
#     print("4. Quit")

# while True:
#     show_menu()
    
#     try:
#         choice = int(input("Choose a menu option (1-4): "))
        
#         if choice == 1:
#             task = input("Enter a task: ")
#             tasks.append(task)
#             print("Task added!")

#         elif choice == 2:
#             if not tasks:
#                 print("No tasks here!")
#             else:
#                 print("Your tasks:")
#                 for i, task in enumerate(tasks, start=1):
#                     print(f"{i}. {task}")

#         elif choice == 3:
#             if not tasks:
#                 print("Nothing here to delete")
#             else:
#                 try:
#                     task_num = int(input("Which task number to delete? "))
#                     if 1 <= task_num <= len(tasks):
#                         deleted = tasks.pop(task_num - 1)
#                         print(f"Deleted: {deleted}")
#                     else:
#                         print("That task number doesn’t exist.")
#                 except ValueError:
#                     print("Enter a number for the task, not a word!")

#         elif choice == 4:
#             print("Bye!")
#             break

#         else:
#             print("That is not an option. Please try again")

#     except ValueError:
#         print("Invalid. Enter numbers only")

#     except Exception as e:
#         print(f"Oops! Something went wrong: {e}")

#     finally:
#         print("Back to the main menu...")
