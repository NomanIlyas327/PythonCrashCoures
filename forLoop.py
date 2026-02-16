#  for loop to print numbers from 1 to 10
for i in range(1, 11):
    print(i)
#  for loop to iterate through a list of fruits
fruits = ["apple", "banana", "cherry", "date"]
for fruit in fruits:
    print(fruit)
#  for loop with else clause
for i in range(5):
    print("Iteration:", i)
else:
    print("Loop completed.")
#  nested for loop to print a multiplication table
for i in range(1, 6):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print("-----")
#  for loop with break statement
userNumber = int(input("Enter a number to find its multiples of 3 up to 30: "))
for i in range(userNumber, 31):
    if userNumber == 5:
        print("Breaking the loop at i =", i)
        break
    print(i)
else:
    print("Loop completed.")
#  for loop with continue statement
for i in range(10):
    if i % 2 == 0:
        continue
    print("Odd number:", i)     
#  for loop to iterate through a dictionary
person = {"name": "Alice", "age": 30, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")
#  for loop to iterate through a string
sample_string = "Python"
for char in sample_string:
    print(char)
#  for loop with range and step
for i in range(0, 20, 2):
    print(i)
#  for loop to calculate the factorial of a number
num = 5
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"Factorial of {num} is {factorial}")
#  for loop to create a list of squares of numbers
squares = []
for i in range(1, 11):
    squares.append(i ** 2)
print("Squares from 1 to 10:", squares)
#  for loop to iterate through a set
unique_numbers = {1, 2, 3, 4, 5}
for number in unique_numbers:
    print("Unique number:", number)
#  for loop to iterate through a tuple
coordinates = (10, 20, 30)
for coord in coordinates:
    print("Coordinate:", coord)
#  for loop with enumerate to get index and value
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(f"Index: {index}, Color: {color}")
#  for loop with zip to iterate through two lists simultaneously
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"Name: {name}, Age: {age}")
# End of for loop examples
print("End of for loop examples.")