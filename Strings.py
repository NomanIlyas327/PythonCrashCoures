# Strings
# basic string operations and manipulations
# Creating strings
str1 = "Hello"
str2 = 'World'
# Concatenation
greeting = str1 + " " + str2
print("Concatenated String:", greeting)
# Repetition
repeat_str = str1 * 3
print("Repeated String:", repeat_str)
# Accessing characters
first_char = str1[0]
print("First Character of str1:", first_char)
last_char = str2[-1]
print("Last Character of str2:", last_char)
# Slicing strings
slice_str = greeting[0:5]
print("Sliced String (0-5):", slice_str)
# String methods
upper_str = greeting.upper()
print("Uppercase String:", upper_str)
lower_str = greeting.lower()
print("Lowercase String:", lower_str)
find_substr = greeting.find("World")        
print("Index of 'World' in greeting:", find_substr)
replace_str = greeting.replace("World", "Python")
print("Replaced String:", replace_str)
split_str = greeting.split(" ")
print("Split String:", split_str)
# String formatting
name = "Alice"
age = 30
formatted_str = "My name is {} and I am {} years old.".format(name, age)
print("Formatted String:", formatted_str)
f_string = f"My name is {name} and I am {age} years old."
print("F-String:", f_string)
# Escape characters
escape_str = "He said, \"Hello!\"\nWelcome to Python."
print("String with Escape Characters:\n", escape_str)
# String length
length_str = len(greeting)
print("Length of greeting string:", length_str)
# rstripping whitespace
whitespace_str = "   Hello World!   "
rstripped_str = whitespace_str.rstrip()
print("Right Stripped String:", rstripped_str)
# lstripping whitespace
lstripped_str = whitespace_str.lstrip()
print("Left Stripped String:", lstripped_str)
# stripping whitespace
stripped_str = whitespace_str.strip()
print("Stripped String:", stripped_str)

# string methods
meetUp = "   MeetUp at the Park   "
count_substr = meetUp.count("a")
print("Count of 'a' in meetUp:", count_substr)
startswith_hello =  meetUp.startswith("   MeetUp")
print("Does  meetUp start with '   MeetUp'?:", startswith_hello)
endswith_python =  meetUp.endswith("Python")
print("Does  meetUp end with 'Python'?:", endswith_python)
# End of String Examples