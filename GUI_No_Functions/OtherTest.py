import tkinter as tk
from tkinter import ttk

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dynamic Task Manager")
        
        self.tasks = []
        
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        self.add_task_btn = tk.Button(self.main_frame, text="Add Task", command=self.add_task)
        self.add_task_btn.pack(pady=10)

        # Create a canvas for the task container
        self.canvas = tk.Canvas(self.main_frame)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Add a scrollbar to the canvas
        self.scrollbar = ttk.Scrollbar(self.main_frame, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configure the canvas to work with the scrollbar
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>', self.on_canvas_configure)

        # Create a frame inside the canvas
        self.task_container = tk.Frame(self.canvas)

        # Add the frame to the canvas
        self.canvas.create_window((0, 0), window=self.task_container, anchor="nw")

        self.save_tasks_btn = tk.Button(self.main_frame, text="Save Tasks", command=self.save_tasks)
        self.save_tasks_btn.pack(pady=10)

    def on_canvas_configure(self, event=None):
        # Update the scroll region to encompass the inner frame
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        
    def add_task(self):
        task_frame = tk.Frame(self.task_container)
        task_frame.pack(pady=5, fill=tk.X)

        task_label = tk.Label(task_frame, text=f"Task {len(self.tasks) + 1}:")
        task_label.pack(side=tk.LEFT)

        task_entry = tk.Entry(task_frame)
        task_entry.pack(side=tk.LEFT, padx=10, fill=tk.X, expand=True)

        remove_btn = tk.Button(task_frame, text="Remove", command=lambda: self.remove_task(task_frame))
        remove_btn.pack(side=tk.LEFT)

        self.tasks.append(task_entry)
        self.on_canvas_configure()  # Update scroll region whenever a new task is added

    def remove_task(self, task_frame):
        task_frame.destroy()
        self.tasks = [task for task in self.tasks if task.master != task_frame]
        self.update_task_labels()
        self.on_canvas_configure()  # Update scroll region whenever a task is removed

    def update_task_labels(self):
        for i, task in enumerate(self.tasks):
            task.master.winfo_children()[0].config(text=f"Task {i + 1}:")

    def save_tasks(self):
        task_list = [task.get() for task in self.tasks if task.get().strip() != ""]
        print("Tasks:", task_list)
        # Here you can save the task_list to a file or process it as needed

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
