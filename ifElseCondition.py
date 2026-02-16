#  If else condition example in Python
# Taking input from the user
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
# End of If else condition example
#  Another example with nested if-else
# Taking input from the user    
number = int(input("Enter an integer number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
# End of Another If else condition example
#  Yet another example with grading system
# Taking input from the user    
marks = int(input("Enter your marks (0-100): "))
if marks >= 90:
    print("Grade: A")   
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
elif marks >= 50:
    print("Grade: E")
else:
    print("Grade: F")
# End of Grading system example
#  Final example with eligibility check
# Taking input from the user
income = float(input("Enter your annual income: "))
if income >= 50000:
    print("You are eligible for the premium credit card.")
else:
    print("You are not eligible for the premium credit card.")
# End of Eligibility check example
# End of If else condition examples
job = input("Enter your job title: ")
if job.lower() == "software engineer":
    print("You are a software engineer.")
elif job.lower() == "data scientist":
    print("You are a data scientist.")
elif job.lower() == "teacher":
    print("You are a teacher.")
else:
    print("Your job title is not recognized.")
    

# checking even or odd 
number = int(input("Enter the number:"))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# leap year check
year = int(input("Enter a year: "))
if year % 4 == 0:
    print(f"{year} is a leap year.")
else:   
    print(f"{year} is not a leap year.")

# simple login system
username = input("Enter your username: ")
password = input("Enter your password: ")
if username == "admin" and  password == "password123":
    print("Login successful!")
else:
    print("Invalid username or password.")

# three greatest numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))    
c = float(input("Enter third number: "))
if a >=b and a >= c:
    print(f"The greatest number is: {a}")
elif b>=a and b >=c:
    print(f"The greatest number is: {b}")
else:    
    print(f"The greatest number is: {c}")

# Triangle type check
side1 = float(input("Enter length of first side: "))
side2 = float(input("Enter length of second side: "))
side3 = float(input("Enter length of third side: "))
total = side1 + side2 + side3
if total == 180:
    if side1 > 0 and side2 > 0 and side3 > 0:
        if side1 == side2 == side3:
            print("The triangle is equilateral.")
        elif side1 == side2 or side2 == side3 or side1 == side3:
            print("The triangle is isosceles.")
        else:
            print("The triangle is scalene.")
    else:
        print("The angles do not form a valid triangle.")
else:
    print("The angles cannot be zero and should sum up to 180 degrees.")


#  Electricity bill calculation
units = float(input("Enter the number of units consumed: "))
if units <=100:
    Bill = units * 5
elif units <= 200:
    Bill = 100 * 5 + (units - 100) * 7
elif units <= 300:
    Bill = 100 * 5 + 100 * 7 + (units - 200) * 10
else:
    Bill = 100 * 5 + 100 * 7 + 100 * 10 + (units - 300) * 15
print(f"Your electricity bill is: {Bill}")


# ATM machine simultaion
pin = input("Enter your PIN: ")
if pin == "1234":
    print("PIN accepted. Welcome to the machine.")
    # Agar PIN sahi hai, toh option de: 1. Check Balance, 2. Withdraw Money.
    options = input("Choose an option (1. Check Balance, 2. Withdraw Money): ")
    if options == "1":
        print("Your balance is $1000.")
    elif options == "2":
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= 1000:
            print(f"You have withdrawn ${amount}. Your remaining balance is ${1000 - amount}.")
        else:
            print("Insufficient balance.")
    else:
        print("Invalid option selected.")
else:
    print("Invalid PIN. Access denied.")

# Quadratic equation solver
import math
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
D = b**2 - 4*a*c
if D > 0:
    print("Roots are Real and Different.")
elif D == 0:
    print("Roots are Real and Same.")
else:    
    print("Roots are Complex\imaginary.") 


#  Rock, Paper, Scissors game
import random
choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)
user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "paper" and computer_choice == "rock") or \
     (user_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
else:
    print("Computer wins!")
