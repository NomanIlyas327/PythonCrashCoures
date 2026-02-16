# tryExcept Example
def divide_numbers(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    else:
        return result
num1 = float(input("Enter the numerator: "))
num2 = float(input("Enter the denominator: "))
division_result = divide_numbers(num1, num2)
print("Result of division:", division_result)
