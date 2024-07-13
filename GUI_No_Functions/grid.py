# This file will be used as an example file for the grid system and buttons in tkinter.

from tkinter import *

root = Tk()

labelOne = Label(root, text = "Hello")
labelTwo = Label(root, text = "Fuck you")

labelOne.grid(row = 0, column=0) #.grid is used to specify the location of a label.
labelTwo.grid(row = 1, column=0)

root.mainloop()

