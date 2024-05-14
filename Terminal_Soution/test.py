import time as T
import threading

"""
New concepts are being learned: Multiprocessing and multithreading.

Thread = Seperate order of instructions. Each thread takes a turn running to achieve concurrency

CPU bound = Program/task spends most of its time waitting for internal events to use multiprocessing.

IO bound = Program/task spends most of its time waiting for external evens use multithreading.
"""

def main():
    print("------------------------")
    print("|Timer and Task manager|")
    print("------------------------")


    while True:
        try:

            mainMenuIn = int(input("Your choice: "))

            match mainMenuIn:
                case 1:
                    task_Manager_Menu_Input()
                case 2:
                    break
                case _:
                    print("Your input is out of bounds. Please try again.")
                    
        except ValueError:
            print("")
            print("You input the wrong data type. You are supposed to input an integer.")
            print("")

def task_Manager_Menu_Input():
    while True: 

        taskManagerInput = int(input("Your choice: "))

        match taskManagerInput:
            case 1:
                taskDetails = input("Input your task: ")

            case 2:
                try:
                    index = int(input("Input index of a task to remove: "))

                except ValueError:
                    print("")
                    print("You need to input an integer value")
                    print("")
                
            case 3:
                print("Yo")

            case 4:
                main()

            case _:
                print("Your input is out of bounds. Please try again.")

if __name__ == "__main__":
    main()