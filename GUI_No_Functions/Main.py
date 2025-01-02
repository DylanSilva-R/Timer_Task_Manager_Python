"""
TODO: Add settings button
TODO: Optimize GUI
"""

import customtkinter
import time
import threading
from CTkMessagebox import CTkMessagebox #Error wth message box: https://stackoverflow.com/questions/48317606/importerror-cannot-import-name-imagetk
from CustomException import CustomException
from Timer import TimerObj

customtkinter.set_default_color_theme("dark-blue")
customtkinter.set_appearance_mode("dark")

class LeftFrame(customtkinter.CTkFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.taskList = []
        self.createGridSystem()
        taskManagerLabel = customtkinter.CTkLabel(self, justify = "center", text = "Task Manager", font = ("inter", 25))
        taskManagerLabel.grid(row = 0, column = 2, sticky = "nsew")
        
        self.createInnerFrame()
        self.createGridSystemInnerFrame()
        self.createScrollableFrame()
        addTaskBtn = customtkinter.CTkButton(self.innerFrame, text = "Add Task", text_color = "white", anchor = "center",fg_color = "#8B8B8B", command =self.addTask)
        addTaskBtn.grid(row = 2, column = 1, padx = 10, pady = 10)

        removeAllTaskBtn = customtkinter.CTkButton(self.innerFrame, text = "Remove All", text_color = "white", anchor = "center",fg_color = "#8B8B8B", command =self.deleteAll)
        removeAllTaskBtn.grid(row = 3, column = 1, padx = 10, pady = 10)       

    def createGridSystem(self):
        self.grid_columnconfigure((0, 1, 2, 3, 4), weight = 1)
        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)

    def createGridSystemInnerFrame(self):
        self.innerFrame.grid_columnconfigure((0, 1, 2), weight = 1)
        self.innerFrame.grid_rowconfigure((0, 1, 2), weight = 1)

    def createInnerFrame(self):
        self.innerFrame = customtkinter.CTkFrame(self, fg_color = "#D9D9D9")
        self.innerFrame.grid(row = 1, column = 0, rowspan = 3, columnspan = 5, padx = 10, pady = 10, sticky = "nsew")

    def createScrollableFrame(self):
        self.taskScrollFrame = customtkinter.CTkScrollableFrame(self.innerFrame)
        self.taskScrollFrame.grid(row = 0, column = 0, rowspan = 2, columnspan = 3, padx = 10, pady = 10, sticky = "nsew")
    
    def addTask(self):
        # Create a frame to contain the entry frame and button.
        taskFrame = customtkinter.CTkFrame(self.taskScrollFrame)
        taskFrame.pack(fill = "x", pady = 5)

        # Create entry field
        self.taskEntry = customtkinter.CTkEntry(taskFrame, placeholder_text = "Enter text", placeholder_text_color = "Black", text_color = "black",fg_color = "#8B8B8B")
        self.taskEntry.pack(side = "left", fill = "x", expand = True, padx = 5)
        self.taskEntry.bind("<Control-a>", self.selectAll)
        self.taskEntry.bind("<Control-A>", self.selectAll)
        self.taskEntry.bind("<Delete>", self.deleteSelected)

        # Create remove button
        removeBtn = customtkinter.CTkButton(taskFrame, text = "Remove", command = lambda: self.removeTask(taskFrame), fg_color="Red", hover = True, hover_color = "#ff9494")
        removeBtn.pack(side = "right", padx = 5)

        self.taskList.append(taskFrame)

    def deleteAll(self):
        # This function deletes all tasks within the task frame.
        for i in self.taskList:
            i.destroy()
        self.taskList.clear()

    def selectAll(self, event):
        widget = event.widget
        widget.select_range(0, 'end')
        return 'break'
    
    def deleteSelected(self, event):
        # Get the current selection in the entry widget that triggered the event
        widget = event.widget
        if widget.selection_present():
            widget.delete(0, 'end')
        # Return 'break' to stop the default behavior
        return 'break'

    def removeTask(self, taskFrame):
        # This function removes a task depending on user selection.
        try:
            if taskFrame in self.taskList:
                self.taskList.remove(taskFrame)
                taskFrame.destroy()
            else:
                raise CustomException("Task not found in the list.")
        except CustomException as ex:
            CTkMessagebox(title = "error", message = ex.message)

class RightFrame(customtkinter.CTkFrame):

    saveHour = 0
    saveMinutes = 0
    saveSeconds = 0

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.running = False
        self.thread = None
        self.elapsedTime = 0
        self.timeLimit = 0

        self.createGridSystem()
        stopwatchLabel = customtkinter.CTkLabel(self, justify = "center",text = "Stopwatch", font = ("inter", 25))
        stopwatchLabel.grid(row = 0, column = 0, columnspan = 5, sticky = "nsew")

        self.createInnerFrame()
        self.createStopwatchFrame()
        self.createButtons()

    def createGridSystem(self):
        self.grid_columnconfigure((0, 1, 2, 3), weight = 1)
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)

    def createGridSystemInnerFrame(self):
        self.innerFrame.grid_columnconfigure((0, 1, 2, 3), weight = 1)
        self.innerFrame.grid_rowconfigure((0, 1, 2, 3), weight = 1)

    def createGridSystemsStopwatchFrame(self):
        self.stopwatchFrame.grid_columnconfigure((0, 1, 2), weight = 1)
        self.stopwatchFrame.grid_rowconfigure((0, 1, 2), weight = 1)

    def createInnerFrame(self):
        self.innerFrame = customtkinter.CTkFrame(self, fg_color = "#D9D9D9")
        self.innerFrame.grid(row = 1, column = 0, rowspan = 4, columnspan = 4, padx = 30, pady = 30, sticky = "nsew")
        self.createGridSystemInnerFrame()
    
    def createStopwatchFrame(self):
        # Recreate the stopwatch entry. Needs to be single input field that automatically inputs colons for the user.

        self.stopwatchFrame = customtkinter.CTkFrame(self.innerFrame, fg_color = "#8B8B8B")
        self.stopwatchFrame.grid(row = 1, column = 0, columnspan = 4, padx = 10, pady = 10, sticky = "nsew")
        
        self.createGridSystemsStopwatchFrame()

        self.timeEntry = customtkinter.CTkEntry(self.stopwatchFrame, placeholder_text = "HH:MM:SS", justify = "center", placeholder_text_color="white")
        self.timeEntry.grid(row =1 , column = 1, padx = 10, pady = 10, sticky = "nsew")
        self.timeEntry.bind("<KeyRelease>", self.formatTime)

    def formatTime(self, event = None):
        content = self.timeEntry.get()

        filteredContent = "".join([ch for ch in content if ch.isdigit()])

        # Add colons dynamically
        if len(filteredContent) > 2:
            filteredContent = filteredContent[:2] + ":" + filteredContent[2:]
        if len(filteredContent) > 5:
            filteredContent = filteredContent[:5] + ":" + filteredContent[5:]
        if len(filteredContent) >= 8:
            filteredContent = filteredContent[:8]  # Limit to hh:mm:ss
        if len(filteredContent) == 8:
            hours, minutes, seconds = map(int, filteredContent.split(":"))

            self.saveHour = hours
            self.saveMinutes = minutes
            self.saveSeconds = seconds

            hoursToSeconds = hours * 3600
            minutesToSeconds = minutes * 60

            self.timeLimit = hoursToSeconds + minutesToSeconds + seconds

            print("Time limit in seconds: " + str(self.timeLimit))


        # Update the entry field and display label
        self.timeEntry.delete(0, customtkinter.END)
        self.timeEntry.insert(0, filteredContent)

    def createButtons(self):
        self.startBtn = customtkinter.CTkButton(self.innerFrame, text = "Start", text_color = "white", fg_color = "#8B8B8B", command = self.start)
        self.startBtn.grid(row = 2, column = 1, padx = 10, pady = 10)

        self.stopBtn = customtkinter.CTkButton(self.innerFrame, text = "Stop", text_color = "white", fg_color = "#8B8B8B", command = self.stop_Time)
        self.stopBtn.grid(row = 2, column = 3, padx = 10, pady = 10)

        self.resetBtn = customtkinter.CTkButton(self.innerFrame, text = "Reset", text_color = "white", fg_color = "#8B8B8B", command = self.resetStopWatch)
        self.resetBtn.grid(row = 3, column = 2, padx = 10, pady = 10)

    def resetStopWatch(self):
        # This function kills thread and resets time.
        #This function needs to delete all data within the entry points and use the original values that the user input.
        self.stop_Time()
       
        self.timeEntry.delete(0, 'end')
        
        originalTime = str(self.saveHour) + ":" + str(self.saveMinutes) + ":" + str(self.saveSeconds)

        self.timeEntry.insert(0, originalTime)

    def start(self):
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self.startStopwWatch)
            self.thread.start()

    def startStopwWatch(self):
        # Might have to cope and create a thread here, instead of using the TimerObj.
        startTime = time.time()
        while self.running and self.elapsedTime < self.timeLimit:
            currentTime = time.time()
            self.elapsedTime += currentTime - startTime
            startTime = currentTime
            if self.elapsedTime >= self.timeLimit:
                self.elapsedTime = self.timeLimit
                self.running = False

                CTkMessagebox(title = "Alert", message = "Times Up!")
                
                break
            print(f"Elapsed time: {self.timeLimit - self.elapsedTime:.2f} s")
            self.updateTime()
            time.sleep(1)
    
    def updateTime(self):
        print("Update time")

        leftTime = self.timeLimit - self.elapsedTime

        secondsToHours = int(leftTime / 3600)
        secondsToMinutes = int(((leftTime/3600) % 1) * 60)
        seconds = int(((((leftTime/3600) % 1) * 60) % 1) * 60)

        self.timeEntry.delete(0, 'end')
        
        originalTime = str(secondsToHours) + ":" + str(secondsToMinutes) + ":" + str(seconds)

        self.timeEntry.insert(0, originalTime)

    def stop_Time(self):
        
        if self.running:
            self.running = False
            if self.thread is not None:
                self.thread.join()

            secondsToHours = int(self.elapsedTime / 3600)
            secondsToMinutes = int(((self.elapsedTime/3600) % 1) * 60)
            seconds = int(((((self.elapsedTime/3600) % 1) * 60) % 1) * 60)

            print(f"Stopped at {secondsToHours:02}:{secondsToMinutes:02}:{seconds:02} seconds")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__() # super() lets you call methods in the super class from a subclass.
        
        self.title("Task manager and stopwatch")
        self.geometry("1000x500")
        self.create_Main_GridSystem()
        self.create_Left_Frame()
        self.create_Right_Frame()

    def create_Main_GridSystem(self):
        self.grid_rowconfigure((0, 1, 2, 3, 4), weight = 1)

        self.grid_columnconfigure((0, 1, 2, 3, 4), weight = 1)
    
    def create_Settings_Button(self):
        print("Settings button")

    def create_Left_Frame(self):
        self.leftFrame = LeftFrame(self, fg_color = "#8B8B8B")
        self.leftFrame.grid(row = 1, column = 0, columnspan = 3, padx = 10, pady = 10, sticky = "nsew")
    
    def create_Right_Frame(self):
        self.rightFrame = RightFrame(self, fg_color = "#8B8B8B")
        self.rightFrame.grid(row = 1, column = 3, columnspan = 3, padx = 10, pady = 10, sticky = "nsew")

app = App()
app.resizable(width = True, height = True)
app.mainloop()