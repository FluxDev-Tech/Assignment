# 1. Movie Ticket Pricing System
def movie_ticket_price(age):
  if age < 12:
    return 100
  elif 13 <= age <= 19:
    return 150
  elif 20 <= age <= 59:
    return 200
  else:
    return 120

# 2. Even or Odd
def even_odd(number):
  if number % 2 == 0:
    return "Even"
  else:
    return "Odd"

# 3. Sum of List
def sum_of_list(numbers):
  total = 0
  for num in numbers:
    total += num
  return total

# 4. Positive, Negative, or Zero
def check_number(number):
  if number > 0:
    return "Positive"
  elif number < 0:
    return "Negative"
  else:
    return "Zero"

# 5. Simple Grading System
def grade(score):
  if score >= 90:
    return "A"
  elif 80 <= score <= 89:
    return "B"
  elif 70 <= score <= 79:
    return "C"
  elif 60 <= score <= 69:
    return "D"
  else:
    return "F"

# 6. Largest of Three Numbers
def largest_of_three(a, b, c):
  if a >= b and a >= c:
    return a
  elif b >= a and b >= c:
    return b
  else:
    return c

# 7. Voting Eligibility
def voting_eligibility(age):
  if age >= 18:
    return "Eligible to vote"
  else:
    return "Not eligible to vote"

# 8. Basic ATM Withdrawal
def atm_withdrawal(balance, withdrawal):
  if balance >= withdrawal:
    return balance - withdrawal
  else:
    return "Insufficient balance"

# 9. Login System
def login(username, password):
  if username == "admin" and password == "1234":
    return "Access granted"
  else:
    return "Access denied"

# 10. Rock, Paper, Scissors Game
import random

def rock_paper_scissors(user_choice):
  choices = ["rock", "paper", "scissors"]
  computer_choice = random.choice(choices)

  if user_choice == computer_choice:
    return "Tie"
  elif (user_choice == "rock" and computer_choice == "scissors") or \
       (user_choice == "paper" and computer_choice == "rock") or \
       (user_choice == "scissors" and computer_choice == "paper"):
    return "You win!"
  else:
    return "Computer wins!"
