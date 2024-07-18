"""
Experimenting with grid layout.
"""
import tkinter as tk
from tkinter import ttk


import tkinter as tk
from tkinter import ttk

class NestedFramesApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x600")
        self.root.title("Nested Frames Example")

        # Create a style object
        style = ttk.Style()
        
        # Configure styles for frames using hexadecimal color values
        style.configure("Outer.TFrame", background="#ADD8E6")  # Light blue
        style.configure("Inner.TFrame", background="#90EE90")  # Light green

        # Outer frame
        self.outer_frame = ttk.Frame(root, style="Outer.TFrame", width=250, height=300, padding="20 20 20 20")
        self.outer_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Inner frame
        self.inner_frame = ttk.Frame(self.outer_frame, style="Inner.TFrame", width=200, height=150, padding="10 10 10 10", borderwidth=2, relief="sunken")
        self.inner_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Add a label to the inner frame
        self.label = ttk.Label(self.inner_frame, text="This is an inner frame", background="#90EE90")
        self.label.pack(pady=20)

        # Add a button to the inner frame
        self.button = ttk.Button(self.inner_frame, text="Click Me")
        self.button.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = NestedFramesApp(root)
    root.mainloop()



"""
if __name__ == "__main__":
    window = tk.Tk()
    window.geometry("600x600")

    # ttk doesn't support background colors as a parameter.
    style = ttk.Style()

    style.configure("outer.TFrame", background = "#8B8B8B")
    style.configure("inner.TFrame", background = "#D9D9D9")

    #Tasks frame
    taskOuterFrame = ttk.Frame(window, style = "outer.TFrame", width =250, height = 250)
    taskOuterFrame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    taskInnerFrame = ttk.Frame(taskOuterFrame, style = "inner.TFrame", width = 150, height = 150)
    taskInnerFrame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    window.mainloop()
"""