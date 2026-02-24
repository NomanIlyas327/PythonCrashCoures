def multiply(a, b):
    return a * b
def add(a, b):
    return a + b
a = 4
b = 5
result_multiply = multiply(a, b)
result_add = add(a, b)
print(f"The result of multiplying {a} and {b} is: {result_multiply}")
print(f"The result of adding {a} and {b} is: {result_add}")

# Age in Days Calculator
def ageindays(age):
    return age * 365    
age = int(input("Enter your age in years: "))
days = ageindays(age)
print(f"You are approximately {days} days old.")

# Even or Odd Checker
def is_even(num):
    return num % 2 == 0
number = int(input("Enter a number: "))
if is_even(number):
    print(f"{number} is an even number.")   
else:  
    print(f"{number} is an odd number.")

def nameformatter(first_name, last_name):
    return f"{first_name} {last_name}"
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = nameformatter(first_name, last_name)

print(full_name.capitalize())


# Vowel Counter
def VowelCounter(input_string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count
user_input = input("Enter a string: ")
vowel_count = VowelCounter(user_input)
print(f"The number of vowels in '{user_input}' is: {vowel_count}")


def finalPrice(original_price, discount_percentage, tax_percentage):
    discount_amount = (discount_percentage / 100) * original_price
    discounted_price = original_price - discount_amount
    tax_amount = (tax_percentage / 100) * discounted_price
    final_price = discounted_price + tax_amount
    return final_price

input_price = float(input("Enter the original price: "))
input_discount = float(input("Enter the discount percentage: "))
input_tax = float(input("Enter the tax percentage: "))
final_price = finalPrice(input_price, input_discount, input_tax)
print(f"The final price after discount and tax is: ${final_price:.2f}")