tasks = []


def get_status_and_get_name(task):
    if task.startswith("[Done]"):
        status = "[Done]"
        task_name = task[7:]
        return status, task_name
    else:
        status = "[Pending]"
        task_name = task
        return status, task_name


def view_task(tasks):
    if len(tasks) == 0:
        print("No tasks to view")
    else:
        for i in range(len(tasks)):
            status, name = get_status_and_get_name(tasks[i])
            print(i + 1, status, name)


def add_task(tasks):
    temp = input("Enter task:")
    tasks.append(temp)


def remove_task(tasks):
    if len(tasks) == 0:
        print("NO tasks to remove")
    else:
        for i in range(len(tasks)):
            print(i + 1, tasks[i])
        try:
            index = int(input("Enter task number to remove"))
        except:
            print("Invalid Task number")
            return
        index -= 1
        if index >= 0 and index < len(tasks):
            tasks.pop(index)
            print("Task removed")
        else:
            print("Invalid task number")


def mark_complete_task(tasks):
    if len(tasks) == 0:
        print("No tasks to complete")
    else:
        for i in range(len(tasks)):
            print(i + 1, tasks[i])
        try:
            index = int(input("Enter which task to mark as complete"))
        except:
            print("Invaild Task number")
            return
        index -= 1
        if 0 <= index < len(tasks):
            if tasks[index].startswith("[Done]"):
                print("Task already complete")
            else:
                tasks[index] = "[Done] " + tasks[index]
                print("Task marked as completed")
        else:
            print("Invalid task number!")


def clearall_task(tasks):
    confirm = input("Are you sure? (y/n): ")
    if confirm.lower() == "y":
        tasks.clear()
        print("All tasks are cleared")
    elif confirm.lower() == "n":
        print("Canceling clear all")
    else:
        print("Invalid option")


def edit_task(tasks):
    for i in range(len(tasks)):
        print(i + 1, tasks[i])
    try:
        index = int(input("Enter which task to modify:")) - 1
    except:
        print("Invalid Task to modify")
        return
    if 0 <= index < len(tasks):
        new_task = input("Enter the edited task: ")
        if tasks[index].startswith("[Done] "):
            tasks[index] = "[Done] " + new_task
        else:
            tasks[index] = new_task
        print("Task is edited")
    else:
        print("Invalid task number")


def search_task(tasks):
    search = input("Enter task to search: ").lower()
    found = False

    for i in range(len(tasks)):
        if search in tasks[i].lower():
            status, name = get_status_and_get_name(tasks[i])
            print(i + 1, status, name)
            found = True

    if not found:
        print("No tasks found")


def done_task(tasks):
    found = False
    for i in range(len(tasks)):
        if tasks[i].startswith("[Done] "):
            status, name = get_status_and_get_name(tasks[i])
            print(i + 1, status, name)
            found = True
    if not found:
        print("No done tasks:(")


def pending_task(tasks):
    found = False
    for i in range(len(tasks)):
        if not tasks[i].startswith("[Done] "):
            status, name = get_status_and_get_name(tasks[i])
            print(i + 1, status, name)
            found = True
    if not found:
        print("No pending tasks:)")
try:
    with open("tasks.txt", "r") as file:
        for line in file:
            tasks.append(line.strip())
except:
    pass
while True:
    print("\n1.Add Task")
    print("2.View Task")
    print("3.Remove Task")
    print("4.Mark as Complete")
    print("5.Clear all Tasks")
    print("6.Edit Task")
    print("7.Search Task")
    print("8.Done Task")
    print("9.Pending Task")
    print("10.Exit")

    try:
        choice = int(input("Enter Your choice:"))
    except:
        print("Invalid Choice")
        continue

    if choice == 1:
        add_task(tasks)
    elif choice == 2:
        view_task(tasks)
    elif choice == 3:
        remove_task(tasks)
    elif choice == 4:
        mark_complete_task(tasks)
    elif choice == 5:
        clearall_task(tasks)
    elif choice == 6:
        edit_task(tasks)
    elif choice == 7:
        search_task(tasks)
    elif choice == 8:
        done_task(tasks)
    elif choice == 9:
        pending_task(tasks)
    elif choice == 10:
        break
    else:
        print("choice not availabe")
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
