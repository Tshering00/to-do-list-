tasks = []
def addTask():
    task = input("Please enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")
    
def listTask():
    if not tasks:
        print("There are no tasks currently.")
    else:
        print("Current tasks:")
        for index, task in enumerate(tasks):
            print(f"Task #{index}. {task}")
            
def deleteTask():
    listTask()   
    try:
        deleteTask = int(input("Enter the task no. to delete: "))
        if deleteTask >= 0 and deleteTask < len(tasks):
            removed_task = tasks.pop(deleteTask)
            print(f"Task '{removed_task}' has been removed.")
        else:
            print("Invalid input! (Out of range.)")
    except ValueError:
        print("Please enter a valid number.")
        
if __name__ == "__main__":
    print("Welcome to my to do list app")
    while True:
        print("\n")
        print("Please select one of the following options:")
        print("---------------------------------------------")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3 List tasks")
        print("4.Exit")
        
        choice = input("Enter your choice: ")
        if (choice == "1"):
            addTask()
        elif(choice == "2"):
            deleteTask()
        elif(choice == "3"):
            listTask()
        elif(choice == "4"):
            break
        else:
            print("Invalid input. Enter the correct one!!")
    print("Goodbyee!!")        
        