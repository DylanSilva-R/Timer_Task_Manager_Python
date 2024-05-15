import sys
import Tasks
import Timer
import threading
import vlc

"""
This is the main file of the timer/task manager program.
This file will handle user input.

TODO:
    - Need to figure out file handling in python.
        -Audio playing: https://stackoverflow.com/questions/20021457/playing-mp3-song-on-python
    - Figure out how to stop and continue time.
    - Then I will be finally done. 
"""
taskObj = Tasks.TasksObj()
timerObj = Timer.TimerObj()

def main():
    print("------------------------")
    print("|Timer and Task manager|")
    print("------------------------")


    while True:
        Main_menu()

        mainMenuIn = int(input("Your choice: "))

        match mainMenuIn:
            case 1:
                task_Manager_Input()
            case 2:
                timer_Menu_Input()
            case 3:
                break
            case _:
                print("Your input is out of bounds. Please try again.")
                    
    sys.exit()

# The three methods below print menu options for the user.
def task_Manager_Menu():
    print("1) Create tasks")
    print("2) Remove tasks")
    print("3) Print Tasks")
    print("4) Back")

def timer_Menu():
    print("1) Set time")
    print("2) Start timing")
    #print("3) Stop time")
    #print("4) Continue Time")
    #print("5) Set alarm sound")
    print("3) Back")

def Main_menu():
    print("1) Task Manager")
    print("2) Timer")
    print("3) Exit")

# Tasks task_Manager_Menu_Input handles user input for tasks management.

def task_Manager_Input():
    while True:  
        task_Manager_Menu()

        taskManagerInput = input("Your choice: ")

        if check_If_Int(taskManagerInput):
            taskManagerConvert = convert_String_To_Int(taskManagerInput)
            match taskManagerConvert:
                case 1:
                    taskDetails = input("Input your task: ")
                    taskObj.add_To_List(taskDetails)

                case 2:
                    if taskObj.get_Task_Count() == 0:
                        print("There are no tasks to remove.")
                    else:
                        index = input("Input index of a task to remove: ")
                        if check_If_Int(index):
                            indexConvert = convert_String_To_Int(index)
                            taskObj.remove_List(indexConvert)
                        else:
                            print("---------------------------------------------------------------")
                            print("You input the wrong data type for your index. Please try again.")
                            print("---------------------------------------------------------------")
                
                case 3:
                    taskObj.print_List()

                case 4:
                    break
                case _:
                    print("Your input is out of bounds. Please try again.")
        else:
            print("---------------------------------------------------------------------------")
            print("Your input the wrong data type for the task manager input. Please try again.")
            print("---------------------------------------------------------------------------")
    
def timer_Menu_Input():
    while True:    
        timer_Menu()

        timerMenuIn = input("Your choice: ")

        if check_If_Int(timerMenuIn):
            convertTimerMenuInput = convert_String_To_Int(timerMenuIn)
            match convertTimerMenuInput:
                case 1:
                    timerObj.check_If_FormatCorrect()
                case 2:
                    if timerObj.get_Time():
                        print("You haven't set a time limit yet. Please do that first.")
                    else:
                        timerThread = threading.Thread(target=timerObj.start_Timer)
                        timerThread.start()

                        timerThread.stop()
                case 3:
                    main()
                case _:
                    print("Your input is out of bounds. Please try again.")
        else:
            print("---------------------------------------------------------------------------")
            print("Your input the wrong data type for the timer menu input. Please try again.")
            print("---------------------------------------------------------------------------")

def set_Alarm_Sound_Input():
    return
       
def check_If_Int(value):
    try:
        convert = int(value)
        return True
    except ValueError:
        return False

def convert_String_To_Int(value):
    return int(value)


if __name__ == "__main__":
    main()
