import time as T


class TimerObj:
    def __init__(self):
        self.newHours = 0
        self.newMinutes = 0
        self.newSeconds = 0

    def get_Time(self):
        if self.newHours == 0 and self.newMinutes == 0 and self.newSeconds == 0:
            return True
        else:
            return False

    def check_If_FormatCorrect(self):
        amountOfTime = input("How much time are you trying to keep track of (Format: HH:MM:SS)? ")
        hours, minutes, seconds = map(int, amountOfTime.split(":"))
        print(f"{hours:02}:{minutes:02}:{seconds:02}")

        self.newHours = hours
        self.newMinutes = minutes
        self.newSeconds = seconds
    
    def start_Timer(self):

        totalSec = self.newHours * 3600 + self.newMinutes * 60 + self.newSeconds

        for countTime in range(totalSec, 0, -1):
            newHour = int(countTime / 3600)
            newMinutes = int(countTime / 60) % 60
            newSeconds = int(countTime % 60)

            #print(f"{newHour:02}:{newMinutes:02}:{newSeconds:02}")
            T.sleep(1)

        print("Times up!")