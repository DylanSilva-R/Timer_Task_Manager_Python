import customtkinter as ctk

class TaskManagerApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x400")
        self.title("Task Manager with Select All and Delete")

        # Outer frame to contain the scrollable frame
        self.outer_frame = ctk.CTkFrame(self)
        self.outer_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Scrollable frame inside the outer frame
        self.scrollable_frame = ctk.CTkScrollableFrame(self.outer_frame)
        self.scrollable_frame.pack(fill="both", expand=True)

        # Button to add tasks
        add_task_button = ctk.CTkButton(self, text="Add Task", command=self.add_task)
        add_task_button.pack(pady=5)

        # List to store task frames
        self.tasks = []

    def add_task(self):
        # Create a frame for each task inside the scrollable frame
        task_frame = ctk.CTkFrame(self.scrollable_frame)
        task_frame.pack(fill="x", pady=5)

        # Create an entry widget for task input
        task_entry = ctk.CTkEntry(task_frame, placeholder_text="Enter Task")
        task_entry.pack(side="left", fill="x", expand=True, padx=5)

        # Bind Control-A and Delete keys to the task_entry
        task_entry.bind("<Control-a>", self.select_all)
        task_entry.bind("<Control-A>", self.select_all)
        task_entry.bind("<Delete>", self.delete_selected)

        # Button to remove the task
        remove_button = ctk.CTkButton(task_frame, text="Remove", command=lambda: self.remove_task(task_frame))
        remove_button.pack(side="right", padx=5)

        # Add the task frame to the list of tasks
        self.tasks.append(task_frame)

    def remove_task(self, task_frame):
        # Remove the task frame from the list and destroy it
        if task_frame in self.tasks:
            self.tasks.remove(task_frame)
            task_frame.destroy()
        else:
            print("Task not found in the list.")

    def select_all(self, event):
        # Select all text in the entry widget that triggered the event
        widget = event.widget
        widget.select_range(0, 'end')
        # Return 'break' to stop the default behavior
        return 'break'

    def delete_selected(self, event):
        # Get the current selection in the entry widget that triggered the event
        widget = event.widget
        if widget.selection_present():
            widget.delete(0, 'end')
        # Return 'break' to stop the default behavior
        return 'break'

if __name__ == "__main__":
    app = TaskManagerApp()
    app.mainloop()
