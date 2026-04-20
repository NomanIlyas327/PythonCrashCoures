import csv
import numpy as np

# Poori class ka average store krnay k liye aik list 
all_averages = []

#File read krna
try: 
    with open(r"Project - Student Marks & Performance Analyzer\students.csv", "r") as file:
        lines = file.readlines()

        #Result file ko loop say bahir likh raha hu ta k result aik hi baar save ho
        with open(r"Project - Student Marks & Performance Analyzer\ result_1.txt", "w") as result_file:
            result_file.write("--- Student Performance Report ---\n\n")

            for line in lines[1:]:
                row = line.strip().split(",")
                if len(row) == 4:
                    name = row[0]
                    math, science, english = int(row[1]),int(row[2]),int(row[3])

                    average = np.mean([math, science, english]) #Numpy say average calculate kiya
                    all_averages.append(average) #List may add krain

                    #Grade logic
                    if average >= 80: grade = "A"
                    elif average >= 60: grade = "B"
                    else : grade = "Fail"

                    #Console or  file dono may output
                    output = f"{name} | Avg:{average:.2f} | Grade {grade}\n"
                    print(output.strip())
                    result_file.write(output)

                    #LOOP K bahar : poori class ka numpy analysis
            if all_averages:
                    class_mean = np.mean(all_averages)
                    class_std = np.std(all_averages)

                        
                        
                    summary = f"\n--- Class Summary ---\nClass Average: {class_mean:.2f}\nClass Std Dev: {class_std:.2f}\n"
                    print(summary.strip())
                    result_file.write(summary)
except FileNotFoundError:
    print("Error: students.csv file nahi mila. Please check the file path.")