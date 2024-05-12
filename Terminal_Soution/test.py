import time as T
import threading

"""
New concepts are being learned: Multiprocessing and multithreading.

Thread = Seperate order of instructions. Each thread takes a turn running to achieve concurrency

CPU bound = Program/task spends most of its time waitting for internal events to use multiprocessing.

IO bound = Program/task spends most of its time waiting for external evens use multithreading.
"""

hours = 0
minutes = 0
seconds = 0

def main():

    checkIfFormatCorrect()
    randomStuff()


    return
def randomStuff():

    while True:
        userIn = input("Input random stuff until the timer stops (Press 3 to escape)")

        if userIn == "3":
            break


def checkIfFormatCorrect():
    amountOfTime = input("How much time are you trying to keep track of (Format: HH:MM:SS)? ")
    hours, minutes, seconds = map(int, amountOfTime.split(":"))

    timerThread = threading.Thread(target = startTimer, args = (hours, minutes, seconds,))
    timerThread.start()

def startTimer(hours, minutes, seconds):
    # Threading will necessary for this method.

    totalSec = hours * 3600 + minutes * 60 + seconds

    for countTime in range(totalSec, 0, -1):
        
        newHour = int(countTime / 3600)
        newMinutes = int(countTime / 60) % 60
        newSeconds = int(countTime % 60)

        print(f"{newHour:02}:{newMinutes:02}:{newSeconds:02}")
        T.sleep(1)

    print("Times up!")

if __name__ == "__main__":
    main()