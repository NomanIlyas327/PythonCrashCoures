marks = [45, 88, 32, 95, 50, 25]
passed_students_marks = [mark for mark in marks if mark >= 50]
print("Passed students marks:", passed_students_marks)

# Challenge 1: The VIP Guest List (Lists + Strings + Comprehension)
guests = ["  ali ", "sara  ", "  AHMED", "biLal  ", "  dua"]
clean_guests = [clean_name.strip() for clean_name in guests]
print(clean_guests)
title_guests = [guest.title() for guest in clean_guests]
print(title_guests)
new_guests = [guest for guest in title_guests if len(guest) > 3]
print(new_guests)



salaries = {"Ali": 50000, "Sara": 65000, "Ahmed": 45000, "Zain": 70000}
for name, salary in salaries.items():
    print(f"{name}: {salary}")

if salary < 60000:
    salary += salary * 0.1
    print(f"{name} got a raise! New salary: {salary}")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_numbers = [num ** 2 for num in numbers if num % 2 != 0]
print("Squared odd numbers:", squared_numbers)