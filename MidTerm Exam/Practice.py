1.

age = int(input("Enter your age: "))

if age < 12:
    price = 100
elif 13 <= age <= 19:
    price = 150
elif 20 <= age <= 59:
    price = 200
else:
    price = 120

print(f"Your movie ticket price is: {price}")


2.

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

3.

numbers = []  
for i in range(5):
    numbers.append(int(input("Enter a number: ")))  

print("The sum of all numbers is:", sum(numbers))

4.


num = float(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

5.


score = int(input("Enter your score (0-100): "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")

6.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

largest = max(num1, num2, num3)

print("The largest number is:", largest)


7.

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

8.

balance = float(input("Enter your account balance: "))

withdrawal = float(input("Enter withdrawal amount: "))

if withdrawal <= balance:
    balance -= withdrawal
    print(f"Withdrawal successful! Your new balance is: {balance:.2f}")
else:
    print("Error: Insufficient funds.")

9.

correct_username = "admin"
correct_password = "1234"

username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username and password == correct_password:
    print("Access granted. Welcome!")
else:
    print("Access denied. Incorrect username or password.")


10.

import random

choices = ["rock", "paper", "scissors"]

user_choice = input("Enter rock, paper, or scissors: ").lower()

computer_choice = random.choice(choices)

print(f"Computer chose: {computer_choice}")

if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "paper" and computer_choice == "rock") or \
     (user_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
else:
    print("You lose!")
