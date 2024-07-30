"""
Experimenting with grid layout.

TODO: Build a scroll bar feature for tasks that the user wants to do.
TODO: 

"""
import tkinter as tk
from customException import *
from tkinter import ttk, font

def checkIfInputIsValid():
    
    '''
        There will be two test cases to check for potential user inputs:
                First: Check if the characters are integers.
                Second: Check if the values are less than 0 and not greater than 100
    '''

    try:

        hoursDigitVal = int(hours.get())
        minutesDigitVal = int(minutes.get())
        secondsDigitVal = int(seconds.get())
        
        if (hoursDigitVal < 0) or (minutesDigitVal < 0) or (secondsDigitVal < 0):
            raise customException("One of your values is below 0.")
        elif (hoursDigitVal > 99) or (minutesDigitVal > 99) or (secondsDigitVal > 99):
            raise customException("One of our values is greater than 99")

    except customException as ex:
        print(ex)
    except ValueError as ex:
        print("You input the wrong data type")

def restStopWatchValues():
    
    
    return


def mainWindowGridSystem(window):
    window.columnconfigure(0, weight = 10)
    window.columnconfigure(1, weight = 1)
    window.columnconfigure(2, weight = 10)
    
    window.rowconfigure(0, weight = 1)
    window.rowconfigure(1, weight = 2)
    window.rowconfigure(2, weight = 1)

def createTaskContainer(window, style):
    """
    The purpose of this function to create the entier task container.
    """

    #First create styles
    style.configure("Custom.TLabel", background = "#8B8B8B", foreground = "white", font = ("inter", 15)) #style for label
    style.configure("Custom.TButton", background = "#8B8B8B", foreground = "white", font = ("inter", 10))
    style.configure("outerFrame.TFrame", background="#8B8B8B") # Stle for outer frame
    style.configure("innerFrame.TFrame", background="#D9D9D9") # Style for inner Frame

    #Create frames and label
    taskOuterFrame = ttk.Frame(window, style="outerFrame.TFrame", width=200, height=200)
    taskOuterFrame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
    taskLabel = ttk.Label(taskOuterFrame,
                          text = "Tasks",
                          style = "Custom.TLabel")

    # Configure the grid for taskOuterFrame
    taskOuterFrame.columnconfigure(0, weight=1)
    taskOuterFrame.columnconfigure(1, weight=1)
    taskOuterFrame.columnconfigure(2, weight=1)
    taskOuterFrame.columnconfigure(3, weight=1)
    taskOuterFrame.columnconfigure(4, weight=1)
    taskOuterFrame.columnconfigure(5, weight=1)
    taskOuterFrame.columnconfigure(6, weight=1)
    taskOuterFrame.rowconfigure(0, weight=1)
    taskOuterFrame.rowconfigure(1, weight=1)
    taskOuterFrame.rowconfigure(2, weight=1)
    taskOuterFrame.rowconfigure(3, weight=2)

    # Fit inner frame and task label into the outer frame.
    taskInnerFrame = ttk.Frame(taskOuterFrame, style="innerFrame.TFrame", width=100, height=100)
    taskInnerFrame.grid(row=1, column=0, columnspan=7, rowspan = 3,padx=10, pady=10, sticky="nsew")
    taskLabel.grid(row=0, column=1, columnspan=5)

    # Create grid for taskInnerFrame
    taskInnerFrame.columnconfigure(0, weight=1)
    taskInnerFrame.columnconfigure(1, weight=1)
    taskInnerFrame.columnconfigure(2, weight=1)
    taskInnerFrame.rowconfigure(0, weight=1)
    taskInnerFrame.rowconfigure(1, weight=1)
    taskInnerFrame.rowconfigure(2, weight=1)

    addTaskButton = ttk.Button(taskInnerFrame, style = "Custom.TButton", text = "Add", width=5)
    addTaskButton.grid(row = 2, column = 0)
    removeTaskButton = ttk.Button(taskInnerFrame, style = "Custom.TButton", text = "Remove", width=8)
    removeTaskButton.grid(row = 2, column = 2)


def createStopWatchContainer(window, style):
    """
    The purpose of this function is to create a container for the stopwatch.
    """

    #Create styles
    style.configure("Custom.TLabel", background = '#8B8B8B', foreground = 'white', font = ("inter", 15))
    style.configure("Custom.TButton", background = "#8B8B8B", foreground = "white", font = ("inter", 10))
    style.configure("outerFrame.TFrame", background="#8B8B8B")
    style.configure("innerFrame.TFrame", background="#D9D9D9")

    #Create frames
    stopwatchOuterFrame = ttk.Frame(window, style = "outerFrame.TFrame", width = 100, height = 100)
    stopwatchOuterFrame.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")
    stopwatchLabel = ttk.Label(stopwatchOuterFrame,
                               text = "Stopwatch",
                               justify="center",
                               style = "Custom.TLabel")

    #Create grid for stopwatchOuterFrame
    stopwatchOuterFrame.columnconfigure(0, weight=1)
    stopwatchOuterFrame.columnconfigure(1, weight=1)
    stopwatchOuterFrame.columnconfigure(2, weight=1)
    stopwatchOuterFrame.columnconfigure(3, weight=1)
    stopwatchOuterFrame.columnconfigure(4, weight=1)
    stopwatchOuterFrame.columnconfigure(5, weight=1)
    stopwatchOuterFrame.columnconfigure(6, weight=1)
    stopwatchOuterFrame.rowconfigure(0, weight=1)
    stopwatchOuterFrame.rowconfigure(1, weight=1)
    stopwatchOuterFrame.rowconfigure(2, weight=1)
    stopwatchOuterFrame.rowconfigure(3, weight=2)

    # Fit stopwatch inner frame and label into outer frame.s
    stopwatchInnerFrame = ttk.Frame(stopwatchOuterFrame, style = "innerFrame.TFrame", width = 100, height = 100)
    stopwatchInnerFrame.grid(row=1, column=0, columnspan=7, rowspan = 3,padx=10, pady=10, sticky="nsew")
    stopwatchLabel.grid(row = 0, column = 0, columnspan=6, padx=10, pady=10)

    #Create grid for stopwatchInnerFrame to place stopwatchDigitsFrame within it.
    stopwatchInnerFrame.columnconfigure(0, weight = 1)
    stopwatchInnerFrame.columnconfigure(1, weight = 1)
    stopwatchInnerFrame.columnconfigure(2, weight = 1)
    stopwatchInnerFrame.columnconfigure(3, weight = 1)
    stopwatchInnerFrame.rowconfigure(0, weight = 1)
    stopwatchInnerFrame.rowconfigure(1, weight = 1)
    stopwatchInnerFrame.rowconfigure(2, weight = 1)
    stopwatchInnerFrame.rowconfigure(3, weight = 1)

    #Fit the frameForDigits into the stowatch innerFrame
    frameForDigits = ttk.Frame(stopwatchInnerFrame, style = "outerFrame.TFrame", width = 170, height=100)
    frameForDigits.grid(row = 0, column = 1, columnspan = 2, rowspan= 2)

    #Create grid system for frameForDigits
    frameForDigits.columnconfigure(0,weight = 1)
    frameForDigits.columnconfigure(1,weight = 2)
    frameForDigits.columnconfigure(2,weight = 1)
    frameForDigits.columnconfigure(3,weight = 2)
    frameForDigits.columnconfigure(4,weight = 1)
    frameForDigits.columnconfigure(5,weight = 2)
    frameForDigits.columnconfigure(6,weight = 1)

    frameForDigits.rowconfigure(0,weight = 1)
    frameForDigits.rowconfigure(1,weight = 2)
    frameForDigits.rowconfigure(2,weight = 1)

    #Create label to represent time in frameForDigits. There will be three entry points all seperated by two labels using a colon.
    hourEntry = ttk.Entry(frameForDigits, textvariable = hours, width = 5)
    minutesEntry = ttk.Entry(frameForDigits, textvariable = minutes, width = 5)
    secondsEntry = ttk.Entry(frameForDigits, textvariable = seconds, width = 5)

    colonOne = ttk.Label(frameForDigits, style = "Custom.TLabel", text = ":")
    colonTwo = ttk.Label(frameForDigits, style = "Custom.TLabel", text = ":")

    #Locate digit entry and colons.

    hourEntry.grid(row = 1, column = 1)
    minutesEntry.grid(row = 1, column = 3)
    secondsEntry.grid(row = 1, column = 5)

    colonOne.grid(row = 1, column = 2)
    colonTwo.grid(row = 1, column = 4)


    #Create buttons to stop, start, and reset the stopwatch. Locate them in the innerStopwatchFrame
    startButton = ttk.Button(stopwatchInnerFrame, style = "Custom.TButton", text = "Start", command = checkIfInputIsValid)
    stopButton = ttk.Button(stopwatchInnerFrame, style = "Custom.TButton", text = "Stop")
    resetButton = ttk.Button(stopwatchInnerFrame, style = "Custom.TButton", text = "Reset")

    startButton.grid(row = 2, column = 1)
    stopButton.grid(row = 2, column = 2)
    resetButton.grid(row = 3, column = 1, columnspan = 2)



if __name__ == "__main__":
    window = tk.Tk()
    window.title("Stopwatch and Task manager no functionality")
    window.geometry("600x600")
    window['background'] = '#1F1C1C'
    style = ttk.Style()
    style.theme_use('alt')

    hours = tk.StringVar()
    hours.set("H")
    minutes = tk.StringVar()
    minutes.set("M")
    seconds = tk.StringVar()
    seconds.set("S")

    style.configure('Custom.TLabel', background = '#8B8B8B', foreground = 'white', font = ("inter", 15))

    titleLabel = ttk.Label(window, 
                           text = "Stopwatch and Task Manager App",
                           justify="center",
                           style = "Custom.TLabel",
                           padding = (10,0,0,0))

    titleLabel.grid(row = 0, column = 0, columnspan = 3, sticky="n")

    mainWindowGridSystem(window)
    createTaskContainer(window, style)
    createStopWatchContainer(window, style)

    window.mainloop()
