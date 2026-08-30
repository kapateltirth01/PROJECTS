def task():
    task=[]
    print("Welcome to the Task Manager app")
    num_task=int(input("How many tasks do you want to add today="))
    for num in range(num_task):
        
        task.append(input(f"enter task {num}:"))
        
    print("Your tasks are successfully added to today's list\n")
    print(f"Your today's task are {task}")

    t=int(input("How do you want to change anything in your tasks?\n press 1 for yes\t"))
    if t==1:
        while True:
            operation=int(input("Enter 1.Update,2.Add,3.Delete,4.View,5.Exit/Stop.:"))
            if operation==2:
                print("What do you want to add?")
                i=input()
                task.append(i)
                print(f"New task list is {task}\n")
            elif operation==1:
                up=input("What do you want to update? ")
                if up in task:
                    ind=task.index(up)
                    new=input("addtask\t ")
                    task[ind]=new
                    print(f"New task list is {task}\n")

            elif operation==3:
                rem = input("What do you want to delete? :")
                if rem in task:
                    ind=task.index(rem)
                    del task[ind]

                print(f"list of tasks:{task}\n")
            elif operation==4:
                print(f"Your today tasks is {task}\n")
            elif operation==5:
                break
            else:
                print("Please select the correct operation.\n")
    


task()          

       
