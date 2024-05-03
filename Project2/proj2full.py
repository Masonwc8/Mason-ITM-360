import mysql.connector
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Foxtrot8",
    database = "STUDENTS"

)

mycursor = mydb.cursor()

class PasswordManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Manager")


        self.users = {
            "user1": ("user1@example.com", "password1"),
            "user2": ("user2@example.com", "password2")
        }
        self.user_database = {
            "admin": {
                "email": "admin@example.com",
                "password": "admin"
            }
        }
        
        self.background_image = tk.PhotoImage(file="/Users/mason./Desktop/ut.png")
        self.background_label = tk.Label(root, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Header Label
        self.header_label = ttk.Label(root, text="Login", font=("Helvetica", 30))
        self.header_label.pack(pady=10)

        # Username
        self.studentid_label = ttk.Label(root, text="Student ID:")
        self.studentid_label.pack()
        self.studentid_entry = ttk.Entry(root)
        self.studentid_entry.pack()

        # Password
        self.password_label = ttk.Label(root, text="Password:")
        self.password_label.pack()
        self.password_entry = ttk.Entry(root, show="*")
        self.password_entry.pack()
        self.show_password_image = tk.PhotoImage(file="/Users/mason./Desktop/eye_open.png")
        self.show_password_image = self.show_password_image.subsample(10,10)  
        self.hide_password_image = tk.PhotoImage(file="/Users/mason./Desktop/eye_closed.png")
        self.hide_password_image = self.hide_password_image.subsample(10,10)
        self.show_password_button = ttk.Button(root, image=self.show_password_image, command=self.toggle_password_visibility)
        self.show_password_button.pack()

        # Login Button
        self.login_button = ttk.Button(root, text="Login", command=self.login)
        self.login_button.pack(pady=10)


        # Sign Up Now Button
        self.signup_button = ttk.Button(root, text="Sign Up Now", command=self.open_sign_up_window)
        self.signup_button.pack(pady=10)

       
    def toggle_password_visibility(self):
        if self.password_entry["show"] == "*":
            self.password_entry.config(show="")
            self.show_password_button.config(image=self.hide_password_image)
        else:
            self.password_entry.config(show="*")
            self.show_password_button.config(image=self.show_password_image)

    def login(self):
        username = self.studentid_entry.get()
        password = self.password_entry.get()
        url = 'http://127.0.0.1:5000/login'
        resp = request.post(url, data={'StudentId':username.get(), 'Password':password.get()})
        # Check if the provided username and password match any registered user's credentials
        if username in self.users:
            if password == self.users[username][1]:
                messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
            else:
                messagebox.showerror("Login Failed", "Incorrect password!")
        else:
            messagebox.showerror("Login Failed", "User not found!")

    def open_sign_up_window(self):
        sign_up_window = tk.Toplevel(self.root)
        sign_up_window.title("Sign Up")

        # Username
        username_label = ttk.Label(sign_up_window, text="Student ID:")
        username_label.pack()
        username_entry = ttk.Entry(sign_up_window)
        username_entry.pack()

        # Email
        email_label = ttk.Label(sign_up_window, text="Email:")
        email_label.pack()
        email_entry = ttk.Entry(sign_up_window)
        email_entry.pack()

        # Password
        password_label = ttk.Label(sign_up_window, text="Password:")
        password_label.pack()
        password_entry = ttk.Entry(sign_up_window, show="*")
        password_entry.pack()

        # GPA
        GPA_label = ttk.Label(sign_up_window, text="GPA:")
        GPA_label.pack()
        GPA_entry = ttk.Entry(sign_up_window)
        GPA_entry.pack()

        # Sign Up Button
        signup_button = ttk.Button(sign_up_window, text="Sign Up", command=lambda: self.sign_up(username_entry.get(), email_entry.get(), password_entry.get(), GPA_entry.get()))
        signup_button.pack(pady=10)

    def sign_up(self, username, email, password, GPA):
        # Placeholder for sign-up logic
        if username in self.users:
            messagebox.showerror("Error", "Student ID already exists!")
            return
        self.users[username] = (email, password,GPA)
        messagebox.showinfo("Success", "Account created successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordManager(root)
    root.mainloop()

