# Typecasting in Python
# Implicit Typecasting means automatic conversion of one data type to another by Python interpreter
# Explicit Typecasting means conversion of one data type to another using predefined functions
# Implicit Typecasting
a = 5          # Integer
b = 2.5        # Float
result = a + b # Implicitly converts 'a' to float
print("Implicit Typecasting Result:", result)
print("Type of Result:", type(result))
# Explicit Typecasting
x = 10         # Integer
y = float(x)   # Explicitly converting integer to float
print("Explicit Typecasting Result:", y)
print("Type of y:", type(y))
# Converting float to integer
z = 7.9
w = int(z)     # Explicitly converting float to integer
print("Explicit Typecasting Result:", w)
print("Type of w:", type(w))
# Converting string to integer
str_num = "15"
int_num = int(str_num)  # Explicitly converting string to integer
print("String to Integer:", int_num)
print("Type of int_num:", type(int_num))
# Converting string to float
str_float = "12.34"
float_num = float(str_float)  # Explicitly converting string to float
print("String to Float:", float_num)
print("Type of float_num:", type(float_num))
# Converting integer to string
int_to_str = str(100)  # Explicitly converting integer to string
print("Integer to String:", int_to_str)
print("Type of int_to_str:", type(int_to_str))
# Converting float to string
float_to_str = str(9.81)  # Explicitly converting float to string
print("Float to String:", float_to_str)
print("Type of float_to_str:", type(float_to_str))
# Note: Invalid conversions will raise errors
# For example, the following line would raise a ValueError
# invalid_conversion = int("abc")
# Uncommenting the line below will cause an error
# invalid_conversion = int("abc")   
# print("Invalid Conversion Result:", invalid_conversion)
# To handle such cases, use try-except blocks
try:
    invalid_conversion = int("abc")
    print("Invalid Conversion Result:", invalid_conversion)
except ValueError:
    print("Error: Cannot convert 'abc' to an integer.")
# End of Typecasting Examples