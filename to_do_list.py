toDoList = [] # creating the list
toDoList.append("car wash") # adding task to list with append
end = False
while not end :
    value=int(input('''
        Please choose a task to perform.
        1.Press 1 to add task in to do list
        2.Print number of tasks in your list 
        3.Remove the first task in your list
        4.Remove a specific task from the list
        5.Clear the whole list
        6.Close the To DO LIST APP
        ''')) # adding, deleting tasks with input()
    match value:
        case 1:
            taskToAdd=str(input("Enter the task you want to add to the list.")) # adding task with input()
            toDoList.append(taskToAdd)
            for items in toDoList:
                print(items)
        case 2: # printing number of tasks
            len(toDoList)
            if len(toDoList) < 4: # if user has less than 4 task
                print("You have",len(toDoList),"tasks to do")
                for items in toDoList:
                    print(items)
                print("You have time to do more tasks.")
            elif len(toDoList) >= 6: # if user has 6 more tasks
                print("You have", len(toDoList), "tasks to do")
                for items in toDoList:
                    print(items)
                print("You have no room to do more tasks.")
            else: # if user has 4 or less than 6 tasks
                for items in toDoList:
                    print(items)
        case 3: # removing first task
            toDoList.pop(0)
            for items in toDoList:
                print(items)
        case 4: # removing specific task from the list
            taskToRemove=str(input("Enter the task you want to remove from list"))
            toDoList.remove(taskToRemove)
            for items in toDoList:
                print(items)
        case 5: # clearing the whole list
            toDoList.clear()
            print("Your list has been cleared, now has",len(toDoList),"tasks in it")
        case 6:
            print("Have a good day working on your tasks")
            end = True


