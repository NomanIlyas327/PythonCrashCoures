import csv
import numpy as np

# File read karna
with open(r"Project - Student Marks & Performance Analyzer\students.csv", "r") as file:
    lines = file.readlines() # Saari lines ki list ban gayi

# Pehli line (Header) ko chor kar loop chalayen
for line in lines[1:]:
    # CLEANING STEP:
    # 1. line.strip() -> faltu spaces/newlines khatam
    # 2. .split(",") -> comma se alag karke list banana
    row = line.strip().split(",")

    # Check karein ke row mein 4 cheezain hain (Name, Math, Science, English)
    if len(row) == 4:
        name = row[0]
        
        # DATA CONVERSION (String to Integer)
        math = int(row[1])
        science = int(row[2])
        english = int(row[3])
        
        # Calculation
        total = math + science + english
        average = total / 3
        print(average)
        
        print(f"{name} ka Average Score: {average:.2f}")

        if average >= 80:
            print(f"{name} Grade: A")
        elif average >=60:
            print(f"{name} Grade: B")
        elif average <= 50:
            print(f"{name} Fail.....")
        
        # NumPy Integration
        Mean = np.mean(total)
        print(Mean)
        standard_deviation = np.std(total)
        print(standard_deviation)

        with open("Project - Student Marks & Performance Analyzer\ results.txt", "w") as result_file:
            result_file.write(f"{name} ka Average Score: {average:.2f}\n")
            if average >= 80:
                result_file.write(f"{name} Grade: A\n")
            elif average >=60:
                result_file.write(f"{name} Grade: B\n")
            elif average <= 50:
                result_file.write(f"{name} Fail.....\n")
            result_file.write(f"Mean: {Mean}\n")
            result_file.write(f"Standard Deviation: {standard_deviation}\n")
            