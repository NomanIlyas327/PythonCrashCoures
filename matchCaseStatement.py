#  Match case statement example in Python 3.10+
# Taking input from the user
day = input("Enter a day of the week (e.g., Monday, Tuesday): ")
match day:
    case "Monday":
        print("It's the start of the work week!")
    case "Tuesday":
        print("It's Tuesday, keep going!")
    case "Wednesday":
        print("It's Wednesday, halfway through the week!")
    case "Thursday":
        print("It's Thursday, the weekend is near!")
    case "Friday":
        print("It's Friday, last day of the work week!")
    case "Saturday":
        print("It's Saturday, enjoy your weekend!")
    case "Sunday":
        print("It's Sunday, get ready for the week ahead!")
    case _:
        print("That's not a valid day of the week.")
# End of Match case statement example

#  Another example using match case for simple calculator
# Taking input from the user
num1 = float(input(" Enter first number: "))
num2 = float(input("Enter second number :"))
operation = input("Enter operation (+, -, *, /): ")
match operation:
    case "+":
        print("addition:", num1 + num2)
    case "-":
        print("subtraction:", num1 - num2)
    case "*":
        print("multiplication:", num1 * num2)   
    case "/":
        if num2 != 0:
            print("division:", num1 / num2)
        else:
            print("Error: Division by zero is not allowed.")
    case _:
        print("Invalid operation selected.")
# End of Another Match case statement example
