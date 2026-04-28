import os

def save_note():
    try:
        # 1. Ye line aapki .py file ka asli rasta (path) nikalegi
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # 2. File ka naam aur folder ka rasta jorein
        filename = os.path.join(script_dir, "notes.txt")
        
        note_text = "Ab ye file wahin banay gi jahan ye code hai!"
        
        with open(filename, "w") as file:
            file.write(note_text)
            
        print(f"✅ Success! File yahan milay gi: {filename}")
        
    except IOError as e:
        print(f"❌ Error: {e}")
    except NameError:
        print("Tip: Agar aap Jupyter Notebook use kar rahe hain toh '__file__' kaam nahi karega.")

save_note()


import os

# Bataye ga ke Python abhi kis folder ko dekh raha hai
current_folder = os.getcwd() 
print(f"Main abhi is folder mein hoon: {current_folder}")

# Check karein ke kya 'notes.txt' exist karti hai?
if os.path.exists("notes.txt"):
    print("Ji haan, file maujood hai!")
else:
    print("File nahi mili.")