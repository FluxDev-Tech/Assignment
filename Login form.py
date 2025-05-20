# importing modules
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Simulated User database
user_db = {"admin": "admin123"}


def handle_login():
    username = username_entry.get()
    password = password_entry.get()

    if username in user_db and user_db[username] == password:
        messagebox.showinfo("Login Successful", f"welcome, {username}!")
    else:
        messagebox.showerror("Login Failed", "Invalid user name or Password")


def open_registration_window():
    def register_user():
        new_username = new_username_entry.get()
        new_password = new_password_entry.get()

        if not new_username or not new_password:
            messagebox.showwarning("Input error", "Please fill out all fields")
            return

        if new_username in user_db:
            messagebox.showerror("Registration Failed", "Username already exist")
        else:
            user_db[new_username] = new_password
            messagebox.showinfo("Registration Successful", "You can now login")
            reg_window.destroy()

    reg_window = tk.Toplevel(root)
    reg_window.title("Register")
    reg_window.geometry("300x200")
    reg_window.resizable(False, False)

    reg_frame = ttk.Frame(reg_window, padding="20")
    reg_frame.pack(expand=True)

    ttk.Label(reg_frame, text="Register", font=("Arial", 14)).grid(row=0, column=0, pady=(0, 10))

    ttk.Label(reg_frame, text="New Username:").grid(row=1, column=0, sticky='w')
    new_username_entry = ttk.Entry(reg_frame, width=30)
    new_username_entry.grid(row=2, column=0, pady=(0, 10))

    ttk.Label(reg_frame, text="New Password:").grid(row=1, column=0, sticky='w')
    new_password_entry = ttk.Entry(reg_frame, width=30, show="*")
    new_password_entry.grid(row=4, column=0, pady=(0, 10))

    register_btn = tk.Button(reg_frame, text="Register", bg="#4CAF50", fg="white", width=28, command=register_user)
    register_btn.grid(row=5, column=0)

root = tk.Tk()
root.title("Login")
root.geometry("300x250")
root.resizable(False, False)

frame = ttk.Frame(root, padding="20")
frame.pack(expand=True)

ttk.Label(frame, text="Login", font=("Arial", 14)).grid(row=0, column=0, pady=(0, 10))

ttk.Label(frame, text="Enter Username:").grid(column=0, row=1, sticky='w')
username_entry = ttk.Entry(frame, width=30)
username_entry.grid(column=0, row=2, pady=(0, 10))

ttk.Label(frame, text="Enter Password:").grid(column=0, row=3, sticky='w')
password_entry = ttk.Entry(frame, show='*', width=30)
password_entry.grid(column=0, row=4, pady=(0, 10))

login_button = tk.Button(frame, text="Log In", bg="#1E90FF", fg="white", width=28, command=handle_login)
login_button.grid(column=0, row=5, pady=(0, 5))

register_button = tk.Button(frame, text="Register", bg="#f0f0f0", width=28, command=open_registration_window)
register_button.grid(column=0, row=6)

root.mainloop()