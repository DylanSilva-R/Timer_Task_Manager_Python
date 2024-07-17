import tkinter as tk
from tkinter import ttk

"""
use this link: https://www.youtube.com/watch?v=mop6g-c5HEY and create the GUI for the application.
left off at layout section - layout intro buttons
this will help me create a frame: https://pythonexamples.org/python-tkinter-frame/ 
"""

class App():
    def __init__(self, window):
        self.window.columnconfigure(0, weight = 1)
        self.window.rowconfigure(1, weght = 1)
        self.window.

        self.createPrimaryLabels(window)
        self.createPrimaryButtons(window)

    def createPrimaryLabels(self, window):
        self.taskLabel = ttk.Label(master = window, text = "Tasks")
        self.taskLabel.pack()

        self.stopwatchLabel = ttk.Label(master = window, text = "Stopwatch")
        self.stopwatchLabel.pack()

    def createPrimaryButtons(self, window):
        
        #Buttons for stopwatch
        self.stopwatchStop = ttk.Button(master = window, text = "Stop")
        self.stopwatchStop.pack()

        self.stopwatchReset = ttk.Button(master = window, text = "Reset")
        self.stopwatchReset.pack()

        self.stopwatchStart = ttk.Button(master = window, text = "Start")
        self.stopwatchStart.pack()

        #Buttons for tasks
        self.tasksAdd = ttk.Button(master = window, text = "Add")
        self.tasksAdd.pack()

        self.tasksRemove = ttk.Button(master = window, text = "Remove")
        self.tasksRemove.pack()




if __name__ == "__main__":
    window = tk.Tk()
    window.title("Stopwatch And Task Manager")
    window.geometry("500x500")
    window['background'] = '#1F1C1C'

    app = App(window)

    window.mainloop()