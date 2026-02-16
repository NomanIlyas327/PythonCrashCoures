# Variables And Data Types in Python with some Examples

# Integer variable
age = 25
print("Age:", age)
print("Type of age:", type(age))
# Float variable
height = 5.9
print("Height:", height)
print("Type of height:", type(height))
# String variable
name = "Alice"
print("Name:", name)
print("Type of name:", type(name))
# Boolean variable
is_student = True
print("Is Student:", is_student)
print("Type of is_student:", type(is_student))
# List variable
fruits = ["apple", "banana", "cherry"]
print("Fruits:", fruits)
print("Type of fruits:", type(fruits))
# Tuple variable
coordinates = (10.0, 20.0)
print("Coordinates:", coordinates)
print("Type of coordinates:", type(coordinates))
# Dictionary variable
person = {"name": "Bob", "age": 30}
print("Person:", person)
print("Type of person:", type(person))
# Set variable
unique_numbers = {1, 2, 3, 4, 5}
print("Unique Numbers:", unique_numbers)
print("Type of unique_numbers:", type(unique_numbers))
# NoneType variable
unknown = None
print("Unknown:", unknown)
print("Type of unknown:", type(unknown))
# Complex variable
complex_number = 3 + 4j
print("Complex Number:", complex_number)
print("Type of complex_number:", type(complex_number))
# Byte variable
byte_data = b"Hello"
print("Byte Data:", byte_data)
print("Type of byte_data:", type(byte_data))
# Bytearray variable
byte_array_data = bytearray(b"Hello")
print("Bytearray Data:", byte_array_data)
print("Type of byte_array_data:", type(byte_array_data))
# Frozenset variable means immutable set and cannot be changed after creation 
frozen_set_data = frozenset([1, 2, 3])  
print("Frozenset Data:", frozen_set_data)
print("Type of frozen_set_data:", type(frozen_set_data))
# Range variable
range_data = range(1, 10)
print("Range Data:", list(range_data))
print("Type of range_data:", type(range_data))
# Memoryview variable
memory_view_data = memoryview(b"Hello")
print("Memoryview Data:", memory_view_data)
print("Type of memory_view_data:", type(memory_view_data))
# Demonstrating variable reassignment
variable = 10
print("Initial variable:", variable)
variable = "Now I'm a string"
print("Reassigned variable:", variable)
print("Type of reassigned variable:", type(variable))
# Demonstrating dynamic typing
dynamic_var = 3.14
print("Dynamic Variable:", dynamic_var)
print("Type of dynamic_var:", type(dynamic_var))
dynamic_var = [1, 2, 3]
print("Reassigned Dynamic Variable:", dynamic_var)
print("Type of reassigned dynamic_var:", type(dynamic_var))
# End of variablesAndDataTypes.py
# Demonstrating type conversion
num_str = "100"
num_int = int(num_str)
print("Converted String to Integer:", num_int)
print("Type of num_int:", type(num_int))
num_float = float(num_str)
print("Converted String to Float:", num_float)
print("Type of num_float:", type(num_float))
# Demonstrating multiple assignments
x, y, z = 1, 2.5, "Hello"
print("x:", x, "Type of x:", type(x))
print("y:", y, "Type of y:", type(y))
print("z:", z, "Type of z:", type(z))
# Demonstrating augmented assignment
count = 10
print("Initial count:", count)
count += 5
print("Updated count after += 5:", count)
count *= 2
print("Updated count after *= 2:", count)
count -= 4
print("Updated count after -= 4:", count)
count /= 2
print("Updated count after /= 2:", count)
# End of variablesAndDataTypes.py