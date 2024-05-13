import time as T
import threading

"""
New concepts are being learned: Multiprocessing and multithreading.

Thread = Seperate order of instructions. Each thread takes a turn running to achieve concurrency

CPU bound = Program/task spends most of its time waitting for internal events to use multiprocessing.

IO bound = Program/task spends most of its time waiting for external evens use multithreading.
"""

def main():
    while True:
        try:

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
                    
                case _:
                    print("Your input is out of bounds. Please try again.")

        except ValueError:
            print("")
            print("You input the wrong data type. You are supposed to input an integer.")
            print("")
            
if __name__ == "__main__":
    main()