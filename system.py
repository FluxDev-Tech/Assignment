import tkinter as tk
from tkinter import messagebox
import time

# Predefined user credentials
users = {
    "admin": "13452",
    "user1": "password",
    "john": "mypassword"
}

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username in users and users[username] == password:
        login_window.destroy()  # Close the login window
        show_grading_window()
    else:
        messagebox.showerror("Login Failed", "Incorrect username or password.")

def calculate_grade():
    try:
        prelim = int(prelim_entry.get())
        midterm = int(midterm_entry.get())
        final = int(final_entry.get())

        if not (0 <= prelim <= 100 and 0 <= midterm <= 100 and 0 <= final <= 100):
            raise ValueError("Grades must be between 0 and 100.")

        final_grade = (prelim * 0.30) + (midterm * 0.30) + (final * 0.40)

        if final_grade < 75:
            numeric_equivalent = 5.0
            remarks = "Failing"
        elif 75 <= final_grade <= 77:
            numeric_equivalent = 3.0
            remarks = "Needs Improvement"
        elif 78 <= final_grade <= 80:
            numeric_equivalent = 2.75
            remarks = "Fair"
        elif 81 <= final_grade <= 83:
            numeric_equivalent = 2.5
            remarks = "Satisfactory"
        elif 84 <= final_grade <= 86:
            numeric_equivalent = 2.25
            remarks = "Good"
        elif 87 <= final_grade <= 89:
            numeric_equivalent = 2.0
            remarks = "Very Good"
        elif 90 <= final_grade <= 92:
            numeric_equivalent = 1.75
            remarks = "Excellent"
        elif 93 <= final_grade <= 95:
            numeric_equivalent = 1.5
            remarks = "Outstanding"
        else:
            numeric_equivalent = 1.25
            remarks = "Excellent with Distinction"

        result_text.config(state=tk.NORMAL) #enable editing
        result_text.delete("1.0", tk.END) #clear text
        result_text.insert(tk.END, f"Final Grade Calculation:\n")
        result_text.insert(tk.END, f"Student Name: {student_name_entry.get()}\n")
        result_text.insert(tk.END, f"Course Section: {course_section_entry.get()}\n")
        result_text.insert(tk.END, f"Prelim Grade: {prelim}\n")
        result_text.insert(tk.END, f"Midterm Grade: {midterm}\n")
        result_text.insert(tk.END, f"Final Exam Grade: {final}\n")
        result_text.insert(tk.END, f"Final Grade: {final_grade:.2f}\n")
        result_text.insert(tk.END, f"Numeric Equivalent: {numeric_equivalent}\n")
        result_text.insert(tk.END, f"Remarks: {remarks}\n")
        result_text.config(state=tk.DISABLED) #disable editing

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

def show_grading_window():
    global student_name_entry, course_section_entry, prelim_entry, midterm_entry, final_entry, result_text
    grading_window = tk.Tk()
    grading_window.title("Grading System")

    student_name_label = tk.Label(grading_window, text="Student Name:")
    student_name_label.grid(row=0, column=0, padx=5, pady=5)
    student_name_entry = tk.Entry(grading_window)
    student_name_entry.grid(row=0, column=1, padx=5, pady=5)

    course_section_label = tk.Label(grading_window, text="Course-Section:")
    course_section_label.grid(row=1, column=0, padx=5, pady=5)
    course_section_entry = tk.Entry(grading_window)
    course_section_entry.grid(row=1, column=1, padx=5, pady=5)

    prelim_label = tk.Label(grading_window, text="Prelim Grade (0-100):")
    prelim_label.grid(row=2, column=0, padx=5, pady=5)
    prelim_entry = tk.Entry(grading_window)
    prelim_entry.grid(row=2, column=1, padx=5, pady=5)

    midterm_label = tk.Label(grading_window, text="Midterm Grade (0-100):")
    midterm_label.grid(row=3, column=0, padx=5, pady=5)
    midterm_entry = tk.Entry(grading_window)
    midterm_entry.grid(row=3, column=1, padx=5, pady=5)

    final_label = tk.Label(grading_window, text="Final Exam Grade (0-100):")
    final_label.grid(row=4, column=0, padx=5, pady=5)
    final_entry = tk.Entry(grading_window)
    final_entry.grid(row=4, column=1, padx=5, pady=5)

    calculate_button = tk.Button(grading_window, text="Calculate Grade", command=calculate_grade)
    calculate_button.grid(row=5, column=0, columnspan=2, pady=10)

    result_text = tk.Text(grading_window, wrap=tk.WORD, state=tk.DISABLED)
    result_text.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

    grading_window.mainloop()


# Login Window
login_window = tk.Tk()
login_window.title("Grading System Login")

username_label = tk.Label(login_window, text="Username:")
username_label.grid(row=0, column=0, padx=5, pady=5)
username_entry = tk.Entry(login_window)
username_entry.grid(row=0, column=1, padx=5, pady=5)

password_label = tk.Label(login_window, text="Password:")
password_label.grid(row=1, column=0, padx=5, pady=5)
password_entry = tk.Entry(login_window, show="*")  # Hide password
password_entry.grid(row=1, column=1, padx=5, pady=5)

login_button = tk.Button(login_window, text="Login", command=login)
login_button.grid(row=2, column=0, columnspan=2, pady=10)

login_window.mainloop()