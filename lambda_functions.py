numbers = [1,2,3,4,5,6,7,8,9,10]

result = list(map(lambda x: "Even" if x % 2 == 0 else "Odd", numbers))

# Apply the lambda function to each number in the list
print("Results:", result)


cubic_numbers = int(input("Enter a number: "))
cubic_numbers = list(map(lambda x: x**3, [cubic_numbers]))
print("Cubic Numbers:", cubic_numbers)


first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
multiply_numbers = list(map(lambda x, y: x * y, [first_number], [second_number]))
print("Multiply Numbers:", multiply_numbers)

nums = [10, 20, 30]
print("Original numbers:", nums)
divide_by_2 = list(map(lambda x: x / 2, nums))
print("Divide by 2:", divide_by_2)

words = ["10", "20", "30"]
print("Original words:", words)
convert_to_int = list(map(lambda x: int(x), words))
print("Convert to integers:", convert_to_int)