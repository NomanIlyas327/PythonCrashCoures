hobbies = ["Coding", "Gaming", "Reading"]
hobbies.append("Swiming")
print(hobbies)
hobbies[1] = "Machine Learning"
print(hobbies)

# pi_value = (3.14, 22/7)
# print(pi_value)
# pi_value[0] = 3


data = [("Ali", 20), ("Sara", 22)]
data.append(("Zain" , 25))
print(data)

# 2. Practice Task: The "Data Cleaner" (Intermediate)
raw_data = [999, 10, 20, 30, 40, 50, -999]
split_raw_data = raw_data[1:-1]
print(tuple(split_raw_data))
split_raw_data_tuple = tuple(split_raw_data)
print(split_raw_data_tuple)

# 3. Practice Task: The "To-Do Manager" (List Methods)

tasks = []
tasks.extend(["code", "eat", "sleep"])
print(tasks)
print("Eat Ka index :", tasks.index("eat"))
tasks.remove("sleep")
print(tasks)
if "gym" in tasks:
    print("Yes! gym is in tasks list")
else:
    print("No! gym in not in the task list")


# . Practice Task: "The Secure System" (Tuple)
user_info = ("admin", "12345", "Pakistan")
# user_info[1] = "0000"  # This would cause a TypeError
# File "e:\Github\PythonCrashCoures\list_tuples.py", line 39, in <module>
#     user_info[1] = "0000"
#     ~~~~~~~~~^^^
# TypeError: 'tuple' object does not support item assignment
username = user_info[0]
print(f"Username: {username}")


# Aaj ka Modified Task (Day 3 Practice):
# Ek list banayen: marks = [45, 78, 90, 33, 65].

# .append() use karke aakhir mein 100 add karein.

# .pop(0) use karke pehla number delete karein.

# Index use karte hue 33 ko badal kar 55 kar dein.

# print(marks) karke dekhein kya results aate hain.


marks = [45, 78, 90, 33, 65]
marks.append(100)
marks.pop(0)
marks[2] = 55
print(marks)    

friends = ["Asad", "Abdul Moizz", "Zunera", "Ayesha", "Hira"]
week_days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
print(friends)
print(friends[::-1])
print(week_days)
print(friends[0])
print(week_days[2])
print(friends[-1])
print(week_days[-3])
print(friends[1:4])
friends.append("Ali")
print(tuple(friends))
split_tuple = week_days[2:5]
print(split_tuple)
# splitting a list into two parts
first_half = friends[:3]
second_half = friends[3:]

# The "List Slicer" Challenge
def get_extremes(my_list):
    tuple_list = tuple(my_list)
    return tuple_list[0], tuple_list[-1]

numbers = [10, 20, 30, 40, 50]
first, last = get_extremes(numbers)
print(f"First element: {first}, Last element: {last}")

# The "Unique Sorter" (Lists + Sets)
def unique_sorted(input_list):
    unique_set = set(input_list)
    sorted_list = sorted(unique_set)
    return sorted_list
my_numbers = [5, 3, 8, 1, 2, 5, 3]
result = unique_sorted(my_numbers)
print(result)

# The "Record Keeper" (List of Tuples)
# Aapko ek loop chalana hai jo sirf un students ke naam print kare jin ke marks 80 se zyada hain.
students = [("Asad", 85), ("Abdul Moizz", 78), ("Zunera", 92), ("Ayesha", 88), ("Hira", 75)]
for name, marks in students:
    if marks > 80:
        print(name + " has scored " + str(marks))


# The Challenge: "The Mandi Analyzer"
user_input = input("Enter a list of numbers separated by spaces: ")
splitied_input = user_input.split()
numbers_list = [int(num) for num in splitied_input]
def max_average(nums):
    min_num = float('inf')
    max_num = 0 
    for p in nums:
        if p < min_num:
            min_num = p
        elif p - min_num > max_num:
            max_num = p - min_num


    average = sum(nums) / len(nums)
    return max_num , average
max_diff, avg = max_average(numbers_list)
print(f"Maximum difference: {max_diff}, Average: {avg}")


