import customtkinter as ctk

class TaskManagerApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Task Manager")
        self.geometry("400x400")

        # List to hold references to task entry widgets
        self.task_entries = []

        # Frame for action buttons
        self.button_frame = ctk.CTkFrame(self)
        self.button_frame.pack(pady=10)

        # Add buttons for task management
        self.add_task_button = ctk.CTkButton(self.button_frame, text="Add Task", command=self.add_task)
        self.add_task_button.grid(row=0, column=0, padx=5)
        self.clear_tasks_button = ctk.CTkButton(self.button_frame, text="Clear Tasks", command=self.clear_tasks)
        self.clear_tasks_button.grid(row=0, column=1, padx=5)

        # Frame to contain task entries
        self.task_frame = ctk.CTkFrame(self)
        self.task_frame.pack(fill="both", expand=True, padx=10, pady=10)

    def add_task(self):
        """Adds a new task entry to the task list."""
        task_entry = ctk.CTkEntry(self.task_frame, width=300)
        task_entry.pack(pady=5)
        self.task_entries.append(task_entry)

    def clear_tasks(self):
        """Removes all tasks from the task frame."""
        for task_entry in self.task_entries:
            task_entry.destroy()  # Destroy each task widget
        self.task_entries.clear()  # Clear the list of tasks


if __name__ == "__main__":
    ctk.set_appearance_mode("System")  # Appearance: "System", "Dark", "Light"
    ctk.set_default_color_theme("blue")  # Theme: "blue", "green", "dark-blue"
    app = TaskManagerApp()
    app.mainloop()
