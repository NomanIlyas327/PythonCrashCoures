#  whileloop 
# A simple while loop that prints numbers from 1 to 5
count = 1
while count <= 5:
    print("Count is:", count)
    count += 1
#  while loop with else clause
num = 1
while num < 4:
    print("Number is:", num)
    num += 1                                                                                
else:
    print("Loop completed.")
#  nested while loop to print a pattern
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(i, end=' ')
        j += 1
    print()
    i += 1
#  while loop with break statement
n = 1
while n <= 10:
    if n == 6:
        print("Breaking the loop at n =", n)
        break
    print(n)
    n += 1
#  while loop with continue statement
m = 0
while m < 10:
    m += 1
    if m % 2 == 0:
        continue
    print("Odd number:", m)
#  while loop to calculate the factorial of a number
number = 5
factorial = 1
i = 1
while i <= number:
    factorial *= i
    i += 1
print(f"Factorial of {number} is {factorial}")
#  while loop to create a list of squares of numbers
squares = []
i = 1
while i <= 10:
    squares.append(i ** 2)
    i += 1
print("Squares from 1 to 10:", squares)
#  while loop to iterate through a string
sample_string = "Python"
index = 0
while index < len(sample_string):
    print(sample_string[index])
    index += 1
#  while loop to iterate through a list
fruits = ["apple", "banana", "cherry", "date"]
index = 0
while index < len(fruits):
    print(fruits[index])
    index += 1
#  while loop to iterate through a dictionary
person = {"name": "Alice", "age": 30, "city": "New York"}
keys = list(person.keys())
index = 0
while index < len(keys):
    key = keys[index]
    print(f"{key}: {person[key]}")
    index += 1  
#  while loop to sum numbers until a certain condition is met
total = 0
i = 1
while True:
    total += i
    if total > 50:
        print("Total exceeded 50, breaking the loop.")
        break
    i += 1
print("Final Total:", total)
#  while loop with user input to find multiples of a number
userNumber = int(input("Enter a number to find its multiples of 4 up to 40: "))
i = userNumber
while i <= 40:
    if userNumber == 7:
        print("Breaking the loop at i =", i)
        break
    print(i)
    i += userNumber
else:
    print("Loop completed.")
# End of while loop examples
