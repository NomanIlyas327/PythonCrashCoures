with open("student.txt", "r") as file: 
    marks_data = file.read()
    print("Marks data read from file:")
    for line in marks_data.splitlines():
        # print(line.strip())
        if not line.strip():
            continue
        name, marks = line.split(",")
        print(f"Student: {name}, Marks: {marks}")
