def say_hello(name):
    return f"Hello, {name}!"
name = input("Enter your name: ")
greeting = say_hello(name)
print(greeting)

# name joiner
def join_names(name1,name2):
    return f"{name1}{name2}"
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = join_names(first_name, last_name)
print(f"Your full name is: {full_name}")
#
# square calculator
def square(number):
    return number ** number
num = float(input("Enter a number to square: "))
result = square(num)
print(f"The square of {num} is: {result}")
new_number = square(5)
print(f"The square of 5 is: {new_number}")

def calculate_interest(principle, rate, time):
    return (principle * rate * time) / 100
p = float(input("Enter the principle amount: "))
r = float(input("Enter the interest rate: "))
t = float(input("Enter the time in years: "))
interest = calculate_interest(p, r, t)
print(f"The interest is: {interest}") 


def can_vote(age):
    if age >= 18:
        return "You are eligible to vote."
    else:
        return "You are not eligible to vote yet."
age = int(input("Enter your age: "))
voting_eligibility = can_vote(age)
print(voting_eligibility)

# The Password Validator
def check_password(password):
    if password and len(password) >= 8 and password.isdigit():
        return "Password is valid."
    else:
        return "Password is invalid. It must be at least 8 characters long and contain only digits."
    
user_password = input("Enter your password: ")
password_check = check_password(user_password)
print(password_check)
# The Multi-Discount Calculator
def final_price(amount, customer_type):
    if customer_type.lower() == "vip":
        return amount * 30 / 100
    elif customer_type.lower() == "Student":
        return amount * 20 / 100
    elif customer_type.lower() == "regular":
        return amount * 10 / 100
    else:        return amount
total_amount = float(input("Enter the total amount: "))
customer_type = input("Enter customer type (VIP, Student, Regular): ")
discounted_price = final_price(total_amount, customer_type)
print(f"The final price for a {customer_type} customer is: {discounted_price}")

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
num = int(input("Enter a number to check if it's prime: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:   
    print(f"{num} is not a prime number.")


def get_average(numbers_list):
    if not numbers_list:
        return 0
    return sum(numbers_list) / len(numbers_list)
numbers = input("Enter a list of numbers separated by commas: ")
numbers_list = [float(num) for num in numbers.split(",")]
average = get_average(numbers_list)
print(f"The average of the numbers is: {average}")
