import tkinter as tk
from tkinter import ttk, messagebox

cus = tk.Tk()
cus.title("Manage Customers")
cus.geometry("800x320")
cus.configure(bg="gray")

#title
title_frame = tk.Frame(cus, bg="green", height=40)
title_frame.pack(fill=tk.X)
tk.Label(title_frame, text="Manage Customers", bg="green", fg="blue", font=("Arial", 16)).pack(pady=5)

#Form Frame
form_frame = tk.Frame(cus, bg="gray")
form_frame.place(x=20, y=60)

labels = ["ID:", "First Name:", "Last Name:", "Tel:", "Email:"]
entries = {}

for i, label in enumerate(labels):
    tk.Label(form_frame, text=label, fg="white", bg="gray", font=("Arial", 10)).grid(row=i, column=0, sticky="e", padx=5, pady=3)
    entry = tk.Entry(form_frame, width=30)
    entry.grid(row=i, column=1, pady=3)
    entries[label[:-1].lower()] = entry

#Clear Button
def clear_entries():
     for entry in entries.values():
         entry.delete(0, tk.END)
tk.Button(form_frame, text="Clear", width=20, bg="green", fg="white", command=clear_entries).grid(row=5, columnspan=2, pady=10)

#Table Frame
table_frame = tk.Frame(cus)
table_frame.place(x=330, y=60, width=440, height=180)

columns = ("ID", "Fullname", "Username", "Tel", "email")
tree = ttk.Treeview(table_frame, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=85)
    tree.pack(fill=tk.BOTH, expand=True)

#Add customer
def add_customer():
    data = [entries['id'].get(), entries['first name'].get() +" "+ entries['last name'].get(), entries['first name'].get(), entries['tel'].get(), entries['email'].get()]
    if any(not item.strip() for item in data):
        messagebox.showwarning("Input Error", "TANGA KABA? LAGYAN MO LAHAT YAN!! HAHAHAHAHA.")
        return
    tree.insert("", tk.END, values=data)
    clear_entries()

# Edit customer
def edit_customer():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Edit Error", "No item selected.")
        return
    data = [entries['id'].get(), entries['first name'].get() +""+ entries['last name'].get(), entries['first name'].get(), entries['tel'].get(), entries['email'].get()]
    tree.item(selected[0], values=data)
    clear_entries()

#Delete Customer
def delete_customer():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Edit Error", "MAHAL MO BA AKO?.")
        return
    tree.delete(selected[0])
    clear_entries()

#Populate Form on selection
def on_select(event):
    selected = tree.selection()
    if not selected:
        return
    values = tree.item(selected[0], 'values')
    entries['id'].delete(0, tk.END)
    entries['id'].insert(0, values[0])
    fullname = values[1].split(" ", 1)
    entries['first name'].delete(0, tk.END)
    entries['first name'].insert(0, fullname[0])
    entries['last name'].delete(0, tk.END)
    entries['last name'].insert(0, fullname[1] if len(fullname) > 1 else "")
    entries['tel'].delete(0, tk.END)
    entries['tel'].insert(0, values[3])
    entries['email'].delete(0, tk.END)
    entries['email'].insert(0, values[4])

tree.bind("<<TreeviewSelect>>", on_select)

#Buttons\
btn_frame = tk.Frame(cus, bg="gray")
btn_frame.place(x=330, y=250)
tk.Button(btn_frame, text="Add", bg="green", fg="white", width=10, command=add_customer).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Edit", bg="blue", fg="white", width=10, command=edit_customer).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Delete", bg="red", fg="white", width=10, command=delete_customer).grid(row=0, column=2, padx=5)

cus.mainloop()