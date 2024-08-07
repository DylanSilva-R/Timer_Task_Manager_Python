import customtkinter as ctk

class EntryWithSelectAll(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Entry Widget with Ctrl+A to Select All")

        # Create the entry widget
        self.entry = ctk.CTkEntry(self, placeholder_text="Type here...")
        self.entry.pack(pady=20, padx=20, fill="x", expand=True)

        # Bind the Control-A key event to select all text
        self.entry.bind("<Control-a>", self.select_all)
        self.entry.bind("<Control-A>", self.select_all)

        # Bind the delete key to delete all text when everything is selected
        self.entry.bind("<Delete>", self.delete_selected)

    def select_all(self, event):
        # Select all text in the entry widget
        self.entry.select_range(0, 'end')
        # Return 'break' to stop the default behavior
        return 'break'

    def delete_selected(self, event):
        # Get the current selection
        if self.entry.selection_present():
            self.entry.delete(0, 'end')
        # Return 'break' to stop the default behavior
        return 'break'

if __name__ == "__main__":
    app = EntryWithSelectAll()
    app.geometry("400x200")
    app.mainloop()