import time
import threading

class Stopwatch:
    def __init__(self, time_limit):
        self.time_limit = time_limit
        self.elapsed_time = 0
        self.running = False
        self.thread = None

    def start(self):
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self.run)
            self.thread.start()

    def run(self):
        start_time = time.time()
        while self.running and self.elapsed_time < self.time_limit:
            current_time = time.time()
            self.elapsed_time += current_time - start_time
            start_time = current_time
            if self.elapsed_time >= self.time_limit:
                self.elapsed_time = self.time_limit
                self.running = False
                print(f"Time limit reached: {self.time_limit} seconds")
                break
            print(f"Elapsed time: {self.elapsed_time:.2f} seconds")
            time.sleep(1)

    def stop(self):
        if self.running:
            self.running = False
            if self.thread is not None:
                self.thread.join()
            print(f"Stopped at {self.elapsed_time:.2f} seconds")

    def reset(self):
        self.stop()
        self.elapsed_time = 0
        print("Reset stopwatch")

    def get_elapsed_time(self):
        return self.elapsed_time

def main():
    print("Stopwatch Program")
    hours = int(input("Input hours: "))
    minutes = int(input("Input minutes: "))
    seconds = int(input("Input seconds: "))

    hoursToSeconds = hours * 3600
    minutesToSeconds = minutes * 60

    stopwatch = Stopwatch(hoursToSeconds + minutesToSeconds + seconds)

    while True:
        print("\nMenu:")
        print("1. Start Timer")
        print("2. Stop Timer")
        print("3. Continue Timer")
        print("4. Reset Timer")
        print("5. Exit")

        choice = input("Your choice: ")

        if choice == '1':
            stopwatch.start()
        elif choice == '2':
            stopwatch.stop()
        elif choice == '3':
            stopwatch.start()
        elif choice == '4':
            stopwatch.reset()
        elif choice == '5':
            stopwatch.stop()
            break
        else:
            print("Invalid choice. Please try again.")

        print(f"Elapsed Time: {stopwatch.get_elapsed_time():.2f} seconds")

if __name__ == "__main__":
    main()