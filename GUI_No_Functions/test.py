from tkinter import *
import tkinter as tk

"""
use this link: https://www.youtube.com/watch?v=YXPyB4XeYLA and create the GUI for the application.
left off at creating buttons
"""

def main():
    root = Tk(className = 'Task Manager + stop Watch') #root window
    root.geometry("500x500")
    root['background'] = '#1F1C1C'


    def testFunction():
        myLabel = Label(root, text = "I just pressed a fucking button, lmfao!")
        myLabel.pack()

    tasksBox = Entry(root) # Text box to input tasks.
    # tasksBox.get() will fetch data from text field.
    tasksBox.pack()

    timeInput = Entry(root)
    timeInput.pack()

    startButton = Button(root, text = "Start Stop Watch", command = testFunction)
    stopButton = Button(root, text = "Stop Stop Watch", command = testFunction )
    resetButton = Button(root, text = "Reset Stop Watch", command = testFunction)

    startButton.pack()
    stopButton.pack()
    resetButton.pack()

    root.mainloop()  #event loop that keeps the GUI present.



if __name__ == "__main__":
    main()