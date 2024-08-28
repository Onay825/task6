tasks= []
completed = []
def add_task ():
    task = input("Entre your task: ")
    tasks.append(task)
    completed.append(False)
    print("your task added succefully")
def view_tasks ():
    for i in range(len(tasks)):
        print(f"task[{i}]:{tasks[i]}")
def delete_task ():
    tasks.remove(input("Entre the task you want to remove it : "))
def mark_completed():
        task_index =int(input("Entre the task to mark as completed"))
        if 0<= task_index and task_index<len(tasks):
            completed[task_index]==True
            print( "task_index"+"task marked as completed!")
        else:
            print("tasks uncompleted ")
   
while True:
    your_choice=input("entreyour choice: ")
    if your_choice=="add":
        add_task()
    elif your_choice=="delete":
        delete_task()
    elif your_choice=="view":
        view_tasks()
    elif your_choice=="mark the completed":
        mark_completed()
    else:
        print("your choice isnot avilable try again in the second update")