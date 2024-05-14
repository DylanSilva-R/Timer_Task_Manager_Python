import time as T
import threading
import Tasks
import Timer

"""
New concepts are being learned: Multiprocessing and multithreading.

Thread = Seperate order of instructions. Each thread takes a turn running to achieve concurrency

CPU bound = Program/task spends most of its time waitting for internal events to use multiprocessing.

IO bound = Program/task spends most of its time waiting for external evens use multithreading.
"""

taskObj = Tasks.TasksObj()
timerObj = Timer.TimerObj()

def main():
    print("------------------------")
    print("|Timer and Task manager|")
    print("------------------------")


    while True:
        try:
            print("Main menu")
            mainMenuInput = int(input("Your choice: "))

            match mainMenuInput:
                case 1:
                    while True:
                        # Task input
                        print("Task stuff")
                        taskManagerInput = int(input("Your choice: "))

                        match taskManagerInput:
                            case 1:
                                taskDetails = input("Input your task: ")
                                taskObj.addToList(taskDetails)

                            case 2:
                                if taskObj.getTaskCount() == 0:
                                    print("There are no tasks to remove.")
                                else:
                                    index = int(input("Input index of a task to remove: "))
                                    taskObj.removeList(index)
                            
                            case 3:
                                taskObj.printList()

                            case 4:
                                break
                            case _:
                                print("Your input is out of bounds. Please try again.")

        except ValueError:
            print("------------------------------")
            print("You input the wrong data type")
            print("------------------------------")


if __name__ == "__main__":
    main()