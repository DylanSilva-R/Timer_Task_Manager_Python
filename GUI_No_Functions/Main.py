"""
TODO: Configure the ctrl+a shortcut.
TODO: Stopwatch needs to start doing stopwatch things.
"""

import customtkinter
from CTkMessagebox import CTkMessagebox #Error wth message box: https://stackoverflow.com/questions/48317606/importerror-cannot-import-name-imagetk

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
        addTaskBtn.grid(row = 2, column = 1)

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

    def selectAll(self, event):
        self.taskEntry.select_range(0, 'end')
        return 'break'
    
    def deleteSelected(self, event):
        if self.taskEntry.select_present():
            self.taskEntry.delete(0, 'end')
        return 'break'

    def removeTask(self, taskFrame):
        if taskFrame in self.taskList:
            self.taskList.remove(taskFrame)
            taskFrame.destroy()
        else:
            print("Task not found in the list.")
    

class RightFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
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
        self.stopwatchFrame.grid_rowconfigure((0, 2, 4, 6), weight = 1)
        self.stopwatchFrame.grid_rowconfigure((1, 3, 5), weight = 2)

    def createInnerFrame(self):
        self.innerFrame = customtkinter.CTkFrame(self, fg_color = "#D9D9D9")
        self.innerFrame.grid(row = 1, column = 0, rowspan = 4, columnspan = 4, padx = 30, pady = 30, sticky = "nsew")
        self.createGridSystemInnerFrame()
    
    def createStopwatchFrame(self):
        self.stopwatchFrame = customtkinter.CTkFrame(self.innerFrame, fg_color = "#8B8B8B")
        self.stopwatchFrame.grid(row = 1, column = 0, columnspan = 4, padx = 10, pady = 10, sticky = "nsew")
        
        self.createGridSystemsStopwatchFrame()

        self.hourEntry = customtkinter.CTkEntry(self.stopwatchFrame, placeholder_text = "h", placeholder_text_color="white", justify = "center")
        self.hourEntry.grid(row = 1, column = 1, padx = 10, pady = 10, sticky = "nsew")
        colonOne = customtkinter.CTkLabel(self.stopwatchFrame, text=":", text_color = "black")
        colonOne.grid(row = 1, column = 2, sticky = "nsew")
        
        self.minutesEntry = customtkinter.CTkEntry(self.stopwatchFrame, placeholder_text = "min", placeholder_text_color="white", justify = "center")
        self.minutesEntry.grid(row = 1, column = 3, padx = 10, pady = 10, sticky = "nsew")
        colonTwo = customtkinter.CTkLabel(self.stopwatchFrame, text=":", text_color = "black")
        colonTwo.grid(row = 1, column = 4, sticky = "nsew")
        
        self.secondsEntry = customtkinter.CTkEntry(self.stopwatchFrame, placeholder_text = "s",  placeholder_text_color="white", justify = "center")
        self.secondsEntry.grid(row = 1, column = 5, padx = 10, pady = 10, sticky = "nsew")

    def createButtons(self):
        self.startBtn = customtkinter.CTkButton(self.innerFrame, text = "Start", text_color = "white", fg_color = "#8B8B8B", command = self.checkIfInputIsCorrect)
        self.startBtn.grid(row = 2, column = 1, padx = 10, pady = 10)

        self.stopBtn = customtkinter.CTkButton(self.innerFrame, text = "Stop", text_color = "white", fg_color = "#8B8B8B")
        self.stopBtn.grid(row = 2, column = 3, padx = 10, pady = 10)

        self.resetBtn = customtkinter.CTkButton(self.innerFrame, text = "Reset", text_color = "white", fg_color = "#8B8B8B")
        self.resetBtn.grid(row = 3, column = 2, padx = 10, pady = 10)

    def checkIfInputIsCorrect(self):
        try:
            hours = int(self.hourEntry.get())            
            minutes = int(self.minutesEntry.get())
            seconds = int(self.minutesEntry.get())

            if (hours < 0) or (minutes < 0) or (seconds < 0):
                raise customException("One of your values is a negative value.") 
            elif (hours > 99) or (minutes > 99) or (seconds > 99):
                raise customException("One of your values if greater than 99")
            
        except customException as ex:
            CTkMessagebox(title = "Error", message = ex.message)
        except (TypeError, ValueError):
            CTkMessagebox(title = "Error", message = "You input the wrong data type. Please enter integers.")


class customException(Exception):
    def __init__(self, message):
        self.message = message

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__() # super() lets you call methods in the super class from a subclass.
        
        self.title("Task manager and stopwatch")
        self.geometry("500x500")
        self.createMainGridSystem()
        self.createLeftFrame()
        self.createRightFrame()

    def createMainGridSystem(self):
        self.grid_rowconfigure((0, 1, 2, 3), weight = 1)

        self.grid_columnconfigure((0, 1, 2, 3), weight = 1)
    
    def createLeftFrame(self):
        self.leftFrame = LeftFrame(self, fg_color = "#8B8B8B")
        self.leftFrame.grid(row = 1, column = 0, columnspan = 2, padx = 10, pady = 10, sticky = "nsew")
    
    def createRightFrame(self):
        self.rightFrame = RightFrame(self, fg_color = "#8B8B8B")
        self.rightFrame.grid(row = 1, column = 2, padx = 10, pady = 10, sticky = "nsew")

app = App()
app.resizable(width = True, height = True)
app.mainloop()
