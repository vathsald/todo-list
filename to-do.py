tasks=[]
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
    print("7.Exit")

    Choice=int(input("Enter Your Choice:"))

    if Choice==1:
        temp=input()
        tasks.append(temp)
    elif Choice==2:
        if len(tasks)==0:
            print("No tasks to view")
        else:
            for i in range(len(tasks)):
                if tasks[i].startswith("[Done] "):
                    print(i+1, "[Done]", tasks[i][7:])
                else:
                    print(i+1, "[Pending]", tasks[i])
    elif Choice==3:
        if len(tasks)==0:
            print("NO tasks to remove")
        else:
            for i in range(len(tasks)):
                print(i+1, tasks[i])
            index=int(input("Enter task number to remove"))
            index-=1
            if index>=0 and index<len(tasks):
                tasks.pop(index)
                print("Task removed")
            else:
                print("Invalid task number")
    elif Choice==4:
        if len(tasks)==0:
            print("No tasks to complete")
        else:
            for i in range(len(tasks)):
                print(i+1, tasks[i])
            index=int(input("Enter which task to mark as complete"))
            index-=1
            if 0<=index<len(tasks):
                if tasks[index].startswith("[Done]"):
                    print("Task already complete")
                else:
                    tasks[index]= "[Done] " + tasks[index]
                    print("Task marked as completed")
            else:
                print("Invalid task number!")
    elif Choice==5:
        tasks.clear()
        print("All tasks are cleared")
    elif Choice==6:
        for i in range(len(tasks)):
            print(i+1, tasks[i])
        index=int(input("Enter which task to modify:"))-1
        if 0<= index < len(tasks):
            new_task = input("Enter the edited task: ")
            if tasks[index].startswith("[Done] "):
                tasks[index] = "[Done] " + new_task
            else:
                tasks[index] = new_task
            print("Task is edited")
        else:
            print("Invalid task number")
    elif Choice==7:
        break
    else:
        print("Choice not availabe")
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task +"\n")