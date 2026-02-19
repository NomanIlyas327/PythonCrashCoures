fruits = {"banana": 50, "apple": 100, "orange": 80}
# Adding a new item to the dictionary
fruits["grape"] = 120
print(fruits)  # Output: {'banana': 50, 'apple': 100, 'orange': 80, 'grape': 120}
print(fruits["banana"])  # Output: 50

# The Fruit Shop
inventory = {"banana": 50, "apple": 100, "orange": 80}
input_item = input("Enter an item to check its stock: ")
if input_item in inventory:
    print(f"{input_item} is in stock with quantity: {inventory[input_item]}")
else:
    print(f"{input_item} is not in stock.")

# Duplicate Remover
numbers = [1, 2, 2, 3, 4, 4, 5, 5, 5, 6]
unique_numbers = set(numbers)
converted_list = list(unique_numbers)
print(f"Unique numbers: {converted_list}")  # Output: Unique numbers: [1, 2, 3, 4, 5, 6]

# Character Counter
user_input = input("Enter a input of String: ")
input_dict = {}
for char in user_input:
    if char in input_dict:
        input_dict[char] += 1
    else:
        input_dict[char] = 1
print(f"Character count: {input_dict}")

# Common Friends
ali_movies = {"Batman", "Inception", "Interstellar"}
sara_movies = {"Inception", "Frozen", "Batman"}
both_same_movies = ali_movies.intersection(sara_movies)
print(f"Movies both Ali and Sara like: {both_same_movies}")  
# Output:
# Movies both Ali and Sara like: {'Inception', 'Batman'}
all_movies = ali_movies.union(sara_movies)
print(f"All movies liked by Ali and Sara: {all_movies}")  
# Output:
# All movies liked by Ali and Sara: {'Inception', 'Frozen', 'Batman'}


string = "animal"
string_dict = {}
for char in string:
    if char in string_dict:
        string_dict[char] += 1
    else:
        string_dict[char] = 1
print(f"Character count in '{string}': {string_dict}")
for char, count in string_dict.items():
    if count == 1:
        print(f"The first non-repeating character is: '{char}'")
        break

