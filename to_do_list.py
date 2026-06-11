tasks=[]
while True:
    print("\n-TO DO LIST")
    print("1.add tasks")
    print("2.view tasks")
    print("3.delete tasks")
    print("4.exit")
    choice=int(input("enter your choice :"))
    if choice==1:
        task= input("enter tasks: ")
        tasks.append(task)
        print("task added!")
    elif choice==2:
        print("\nyour tasks:")
        for task in tasks:
            print("-",task)
    elif choice==3:
        task_number=int(input("enter task number to delete"))
        tasks.pop(task_number-1)
    elif choice==4:
        print("byee!")
        break

        