import tkinter as tk
from tkinter import messagebox

class TaskManagerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Task Manager")
        
        # Create widgets
        self.username_label = tk.Label(master, text="Username:")
        self.username_entry = tk.Entry(master)
        self.password_label = tk.Label(master, text="Password:")
        self.password_entry = tk.Entry(master, show="*")
        self.login_button = tk.Button(master, text="Login", command=self.login)
        # Add more widgets for task management
        
        # Grid layout
        self.username_label.grid(row=0, column=0)
        self.username_entry.grid(row=0, column=1)
        self.password_label.grid(row=1, column=0)
        self.password_entry.grid(row=1, column=1)
        self.login_button.grid(row=2, column=0, columnspan=2)

    def login(self):
        # Implement login functionality
        username = self.username_entry.get()
        password = self.password_entry.get()
        # Call backend to verify login credentials
        messagebox.showinfo("Login", "Login successful!")  # Placeholder

def main():
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()