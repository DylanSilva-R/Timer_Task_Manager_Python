import time
import threading

class TimerObj:

    def __init__(self):
        self.timeLimit = 0
        self.elapsedTime = 0
        self.running = False
        self.thread = None

    def check_If_FormatCorrect(self):
        while True:

            amountOfTime = input("How much time are you trying to keep track of (Format: HH:MM:SS)? ")
            hours, minutes, seconds = map(int, amountOfTime.split(":"))
            print(f"The time you input: {hours:02}:{minutes:02}:{seconds:02}")
            
            while True:
                yOrNo =input("Is that correct(Y or N)? ")
                
                if yOrNo == "Y" or yOrNo == "y":
                    
                    hoursToSeconds = hours * 3600
                    minutesToSeconds = minutes * 60

                    self.timeLimit = hoursToSeconds + minutesToSeconds + seconds
                    
                    break
                elif yOrNo != "N" or yOrNo != "n":
                    print("Your input is incorrect.")
            break
    
    def set_Time(self, hours, minutes, seconds):
        hoursToSeconds = hours * 3600
        minutesToSeconds = minutes * 60

        self.timeLimit = hoursToSeconds + minutesToSeconds + seconds

    def start(self):
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self.run)
            self.thread.start()

    def run(self):
        startTime = time.time()
        while self.running and self.elapsedTime < self.timeLimit:
            currentTime = time.time()
            self.elapsedTime += currentTime - startTime
            startTime = currentTime
            if self.elapsedTime >= self.timeLimit:
                self.elapsedTime = self.timeLimit
                self.running = False
                print("__________")
                print("|Times Up|")
                print("__________")
                
                break
            print(f"Elapsed time: {self.elapsedTime:.2f} seconds")
            time.sleep(1)

    def stop(self):
        if self.running:
            self.running = False
            if self.thread is not None:
                self.thread.join()

            secondsToHours = int(self.timeLimit / 3600)
            secondsToMinutes = int(((self.timeLimit/3600) % 1) * 60)
            seconds = int(((((self.timeLimit/3600) % 1) * 60) % 1) * 60)

            print(f"Stopped at {secondsToHours:02}:{secondsToMinutes:02}:{seconds:02} seconds")

    def get_elapsed_time(self):
        return self.elapsedTime
    
    def reset(self):
        self.stop()
        self.elapsed_time = 0
        print("Reset stopwatch")

    def check_If_Elapsed_Time_Empty(self):
        if self.timeLimit == 0:
            return True
        else:
            return False
