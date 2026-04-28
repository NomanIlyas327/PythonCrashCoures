import os

def diary_app():
    print("----Personal Diary----")
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_name = os.path.join(script_dir , "diary.txt")
    choice = input("Type 'W' to Write or 'R' to Read: ").upper()
    if choice == 'W':
        write = input("Enter the text you need to write in Diary: ")
        with open(file_name, "w")as file:
            file.write(write)
            print(f"Text '{write}' added to the Diary")
    elif choice == "R":
        try:
            with open(file_name, "r")as f:
               print("\nYour Past Entries:\n" + f.read())
        except FileNotFoundError:
            print("\nError: Diary file abhi bani hi nahi. Pehle kuch likhein!")
    else:
        print("Invalid Choice!")

diary_app()