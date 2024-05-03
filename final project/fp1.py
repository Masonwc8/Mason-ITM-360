import tkinter as tk
import requests

def login():
    response = requests.post('http://localhost:5000/login', json={
        'username': username_entry.get(),
        'password': password_entry.get()
    })
    result_label.config(text=response.json().get('message'))

app = tk.Tk()
app.title("User Login")

tk.Label(app, text="Username:").pack()
username_entry = tk.Entry(app)
username_entry.pack()

tk.Label(app, text="Password:").pack()
password_entry = tk.Entry(app, show='*')
password_entry.pack()

login_button = tk.Button(app, text="Login", command=login)
login_button.pack()

result_label = tk.Label(app, text="")
result_label.pack()

app.mainloop()
