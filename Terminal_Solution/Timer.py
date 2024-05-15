import time as T


class TimerObj:
    totalTime = 0

    def __init__(self):
        self.newHours = 0
        self.newMinutes = 0
        self.newSeconds = 0

    def get_Time(self):
        # Check if time has been inputted or not.
        if self.newHours == 0 and self.newMinutes == 0 and self.newSeconds == 0:
            return True
        else:
            return False

    def check_If_FormatCorrect(self):

        while True:

            amountOfTime = input("How much time are you trying to keep track of (Format: HH:MM:SS)? ")
            hours, minutes, seconds = map(int, amountOfTime.split(":"))
            print(f"The time you input: {hours:02}:{minutes:02}:{seconds:02}")
            
            while True:
                yOrNo =input("Is that correct(Y or N)? ")
                
                if yOrNo == "Y" or yOrNo == "y":
                    
                    self.newHours = hours
                    self.newMinutes = minutes
                    self.newSeconds = seconds
                    
                    break
                elif yOrNo != "N" or yOrNo != "n":
                    print("Your input is incorrect.")
            break
            

    def stop_Time(self):
        saveHours = 0
        saveMinute = 0
        saveSecond = 0
    
    def continue_Time(self):
        return
    
    def start_Timer(self):

        totalSec = self.newHours * 3600 + self.newMinutes * 60 + self.newSeconds

        for countTime in range(totalSec, 0, -1):
            newHour = int(countTime / 3600)
            newMinutes = int(countTime / 60) % 60
            newSeconds = int(countTime % 60)

            #print(f"{newHour:02}:{newMinutes:02}:{newSeconds:02}")
            T.sleep(1)
        print("-----------")
        print("|Times up!|")
        print("-----------")