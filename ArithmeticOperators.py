# Arithmetic Operators in Python with Examples
# Addition
a = 10
b = 5
result = a + b
print("Addition:", result)
# Subtraction
result = a - b
print("Subtraction:", result)
# Multiplication
result = a * b
print("Multiplication:", result)
# Division
result = a / b
print("Division:", result)
# Floor Division
result = a // b
print("Floor Division:", result)
# Modulus
result = a % b
print("Modulus:", result)
print("Type of Modulus:", type(result))
# Exponentiation
result = a ** b
print("Exponentiation:", result)

# Calculator Example
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
 
print("if you want to perform Addition then press +")
print("if you want to perform Subtraction then press -")
print("if you want to perform Multiplication then press *")
print("if you want to perform Division then press /")
operation = input("Enter operation (+, -, *, /): ")

if operation == '+':
    print("Addition:", number1 + number2)
elif operation == '-':
    print("Subtraction:", number1 - number2)
elif operation == '*':
    print("Multiplication:", number1 * number2)
elif operation == '/':
    if number2 != 0:
        print("Division:", number1 / number2)
    else:
        print("Error: Division by zero is not allowed.")
        


