"""
Experimenting with grid layout.
"""
import tkinter as tk
from tkinter import ttk




if __name__ == "__main__":
    window = tk.Tk()
    window.geometry("600x600")

    labelOne = ttk.Label(window, text = "Label One", background = "#ff0000")
    labelTwo = ttk.Label(window, text = "Label Two", background = "#0033ff")
    labelThree = ttk.Label(window, text = "Label Three", background = "#d700ff")
    labelFour = ttk.Label(window, text = "Label Four", background = "#000000")
    labelFive = ttk.Label(window, text = "Label Five", background = "#00857c")
    labelSix = ttk.Label(window, text = "Label Six", background = "#2b8500")
    labelSeven = ttk.Label(window, text = "Label Seven", background = "#5e8500")
    labelEight = ttk.Label(window, text = "Label Eight", background = "#8fa658")

    window.columnconfigure(0, weight = 1)
    window.columnconfigure(1, weight = 1)
    window.rowconfigure(0, weight = 1)
    window.rowconfigure(1, weight = 2)
    window.rowconfigure(2, weight = 1)

    labelOne.grid(row = 0, column = 0, sticky = "nsew")
    labelTwo.grid(row = 0, column = 1, sticky = "nsew")
    labelThree.grid(row = 1, column = 0, sticky = "nsew") 
    labelFour.grid(row = 1, column = 1, sticky = "nsew")
    labelFive.grid(row = 2, column = 0, sticky = "nsew")
    labelSix.grid(row = 2, column = 1, sticky = "nsew")
    labelSeven.grid(row = 3, column = 0, sticky = "nsew")
    labelEight.grid(row = 3, column = 1, sticky = "nsew")




    # ttk doesn't support background colors as a parameter.
    style = ttk.Style()

    style.configure("outer.TFrame", background = "#8B8B8B")
    style.configure("inner.TFrame", background = "#D9D9D9")

    #Tasks frame
    #taskOuterFrame = ttk.Frame(window, style = "outer.TFrame", width =250, height = 250)
    #taskOuterFrame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    #taskInnerFrame = ttk.Frame(taskOuterFrame, style = "inner.TFrame", width = 150, height = 150)
    #taskInnerFrame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    window.mainloop()
