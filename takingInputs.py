#  Taking Inputs from the User in Python
# Using input() function to take input from the user
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello,", name + "!")
print("You are", age, "years old.")
# Note: The input() function returns data as a string
# To take numerical input, we need to convert the string to the appropriate type
# Taking integer input
num1 = int(input("Enter an integer number: "))
num2 = int(input("Enter another integer number: "))
sum_result = num1 + num2
print("The sum of", num1, "and", num2, "is:", sum_result)
# Taking float input
float1 = float(input("Enter a floating-point number: "))
float2 = float(input("Enter another floating-point number: "))
float_sum = float1 + float2
print("The sum of", float1, "and", float2, "is:", float_sum)
# Taking multiple inputs in a single line
input_values = input("Enter multiple numbers separated by spaces: ")
numbers = list(map(int, input_values.split()))
print("You entered the numbers:", numbers)
total = sum(numbers)
print("The total sum of the entered numbers is:", total)
# End of Taking Inputs Examples