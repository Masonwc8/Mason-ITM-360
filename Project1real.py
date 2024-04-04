import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

class PasswordManager:
    def __init__(self, root):
        self.root = root 
        self.root.title("Password Manager")


        
        # Database of registered users (username, email, password) 
        # To return registered users in database; need to call the connection to database through mysql.connector.connect()
        # then wrap the returned records in python objects to allow following condition checks: -10 pts
        self.users = {
            "user1": ("user1@example.com", "password1"),
            "user2": ("user2@example.com", "password2")
        }
        self.user_database = {     #similarly, for change_password button's functionality, missing a db connection: -10pts
            "admin": {
                "email": "admin@example.com",
                "password": "admin"
            }
        }
        
        self.background_image = tk.PhotoImage(file="/Users/mason./Desktop/vape.png")
        self.background_label = tk.Label(root, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Header Label
        self.header_label = ttk.Label(root, text="Login", font=("Helvetica", 30))
        self.header_label.pack(pady=10)

        # Username
        self.username_label = ttk.Label(root, text="Username:")
        self.username_label.pack()
        self.username_entry = ttk.Entry(root)
        self.username_entry.pack()



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

        self.orr = ttk.Label (root, text="--OR--")
        self.orr.pack(pady=10)
    
        self.dont = ttk.Label (root, text="Don't have an Account?...",foreground="cyan")
        self.dont.pack(pady=10)

        # Sign Up Now Button
        self.signup_button = ttk.Button(root, text="Sign Up Now", command=self.open_sign_up_window)
        self.signup_button.pack(pady=10)

       
         # Forget Password Button
        self.forget_password_button = ttk.Button(root, text="Forget Password?", command=self.open_forget_password_window)
        self.forget_password_button.pack(pady=10)

    def toggle_password_visibility(self):
        if self.password_entry["show"] == "*":
            self.password_entry.config(show="")
            self.show_password_button.config(image=self.hide_password_image)
        else:
            self.password_entry.config(show="*")
            self.show_password_button.config(image=self.show_password_image)

    def open_forget_password_window(self):
        forget_password_window = tk.Toplevel(self.root)
        forget_password_window.title("Forget Password")

        # Username
        username_label = ttk.Label(forget_password_window, text="Username:")
        username_label.pack()
        username_entry = ttk.Entry(forget_password_window)
        username_entry.pack()

        # Email
        email_label = ttk.Label(forget_password_window, text="Email:")
        email_label.pack()
        email_entry = ttk.Entry(forget_password_window)
        email_entry.pack()

        # New Password
        new_password_label = ttk.Label(forget_password_window, text="New Password:")
        new_password_label.pack()
        new_password_entry = ttk.Entry(forget_password_window, show="*")
        new_password_entry.pack()

        # Confirm New Password
        confirm_password_label = ttk.Label(forget_password_window, text="Confirm New Password:")
        confirm_password_label.pack()
        confirm_password_entry = ttk.Entry(forget_password_window, show="*")
        confirm_password_entry.pack()

        # Change Password Button
        change_password_button = ttk.Button(forget_password_window, text="Change Password", command=lambda: self.change_password(username_entry.get(), email_entry.get(), new_password_entry.get(), confirm_password_entry.get()))
        change_password_button.pack(pady=10)

    def change_password(self, username, email, new_password, confirm_password):
        # Check for missing entries
        if not all([username, email, new_password, confirm_password]):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        # Check if user exists in the database
        if username not in self.user_database or self.users:
            messagebox.showerror("Error", "User does not exist.")
            return

        # Check if email matches the one in the database
        if email != self.user_database[username]["email"]:
            messagebox.showerror("Error", "Incorrect email address.")
            return

        # Check if new password matches confirm password
        if new_password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match.")
            return

        # Update password in the database
        self.user_database[username]["password"] = new_password
        messagebox.showinfo("Success", "Password has been changed.")

        # Add your forget password widgets here

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

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
        username_label = ttk.Label(sign_up_window, text="Username:")
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

        # Confirm Password
        confirm_password_label = ttk.Label(sign_up_window, text="Confirm Password:")
        confirm_password_label.pack()
        confirm_password_entry = ttk.Entry(sign_up_window, show="*")
        confirm_password_entry.pack()

        # Sign Up Button
        signup_button = ttk.Button(sign_up_window, text="Sign Up", command=lambda: self.sign_up(username_entry.get(), email_entry.get(), password_entry.get(), confirm_password_entry.get()))
        signup_button.pack(pady=10)

    def sign_up(self, username, email, password, confirm_password):
        # Placeholder for sign-up logic
        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match!")
            return
        if username in self.users:
            messagebox.showerror("Error", "Username already exists!")
            return
        self.users[username] = (email, password)
        messagebox.showinfo("Success", "Account created successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordManager(root)
    root.mainloop()


#MySQL
db = mysql.connector.connect(host = 'localhost',
                               user = 'root', 
                               password = 'Foxtrot8')
                               
db.close()                            

DataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="Foxtrot8"
)
cursor = DataBase.cursor()

loginDB = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="Foxtrot8",
  database = 'Logins' 
)

cursor = loginDB.cursor()

loginRecord = """CREATE TABLE ADMINDATA ( 
                   EMAIL  VARCHAR(50) NOT NULL, #VARCHAR(len) sql datatype for string chars
                   PASSWORD VARCHAR(20) NOT NULL,
                   USERID VARCHAR(20), 
                   )
                   """

cursor.execute(loginRecord)

sql = "INSERT INTO ADMINDATA (EMAIL, PASSWORD, USERID) VALUES (%s, %s)" # 3 paramters with 2 values inputs? -3 pts
test_student = ('Mia', '123456')
cursor.execute(sql, test_student)

loginDB.commit()

set_key = "ALTER TABLE ADMINDATA ADD EMAIL VARCHAR(50) NOT NULL PRIMARY KEY"
cursor.execute(set_key)

DataBase.commit()


