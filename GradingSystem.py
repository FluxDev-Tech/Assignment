import time 

# Predefined user credentials
users = {
    "admin": "13452",
    "user1": "password",
    "john": "mypassword"
}

# Welcome Message
print("=" * 35)
print("\n")
print("WELCOME TO GRADING SYSTEM LOGIN")
print("\n")
time.sleep(1)

# Login function
def login():
    attempts = 3
    while attempts > 0:
        print("=" * 35)
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username in users and users[username] == password:
            print("\nLogin Successful!")
            return True
        else:
            attempts -= 1
            print(f"Incorrect username or password. Attempts left: {attempts}\n")

        if attempts == 0:
            print("\nToo many failed attempts. Exiting...")
            print("=" * 35)
            return False

# Main Program
if login():
    # Login successful, continue to grading system
    print("=" * 35)
    print("\nWelcome to the Grading System!\n")
    time.sleep(1)
    
    # Rest of your grading system code here
    while True:
        print("=" * 35)
        student_name = input("Enter Student's Name: ")
        course_section = input("Enter Course-Section: ")
        prelim_grade = int(input("Enter Prelim Exam Grade (0-100): "))
        midterm_grade = int(input("Enter Midterm Exam Grade (0-100): "))
        final_exam_grade = int(input("Enter Final Exam Grade (0-100): "))
        print("=" * 35)
        print("\n")
        

        # Calculate Final Grade
        final_grade = (prelim_grade * 0.30) + (midterm_grade * 0.30) + (final_exam_grade * 0.40)

        # Determine remarks and numeric equivalent
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
      

        # Display final results
        print("=" * 35)
        print("Final Grade Calculation:")
        print(f"Student Name: {student_name}")
        print(f"Course Section: {course_section}")
        print(f"Prelim Grade: {prelim_grade}")
        print(f"Midterm Grade: {midterm_grade}")
        print(f"Final Exam Grade: {final_exam_grade}")
        print(f"Final Grade: {final_grade:.2f}")
        print(f"Numeric Equivalent: {numeric_equivalent}")
        print(f"Remarks: {remarks}")
        print("=" * 35)
        print("\n")

        # Ask if the user wants to calculate another student's grade
        cont = input("Do you want to calculate another grade? (yes/no): ").lower()
        print("\n")
        if cont != 'yes':
            break
else:
    # Exit message after failed login attempts
    print("\nExiting the program. Goodbye!")