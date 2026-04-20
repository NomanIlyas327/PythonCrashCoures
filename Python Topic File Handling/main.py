# 'r': Read (default)

# 'w': Write (purana data delete kar deta hai)

# 'a': Append (nayi cheezein end mein add karta hai)
# Reading a file
with open("test.txt", "r") as file:
    content = file.read()
    print("File ka data ye raha:")
    print(content)

# # Writing to a file
with open("test.txt", "a") as file:
    file.write("yeh ek naya data hai")
with open("test.txt", "r") as file:
    content = file.read()
    print("\nFile ka data ye raha:")
    print(content)

# # Nayi file likhna
lines_to_write = ["ML Model accuracy: 95%\n", "Training time: 2 mins\n"]

with open("output.txt", "w") as file:
    file.writelines(lines_to_write)

# # Data add karna (Append)
with open("output.txt", "a") as file:
    file.write("Epochs: 50\n")

print("Data save ho gaya!")
print("\nFile ka data ye raha:")
with open("output.txt", "r") as file:
    content = file.read()
    print(content)



data_to_write = ["This is some sample data to write to the file.\n", "You can add multiple lines of text.\n", "File handling is important in Python.\n"]
with open("output1.txt", "w") as file:
    file.writelines(data_to_write)

with open("output1.txt", "a") as file:
    file.write("This line is added to the file.\n")

print("Data has been written to output1.txt")
with open("output1.txt", "r") as file:
    content = file.read()
    print("\nContent of output1.txt:")
    print(content)


import json

# Dictionary ko JSON file mein save karna
config = {
    "model": "RandomForest",
    "n_estimators": 100,
    "random_state": 42
}

with open("config.json", "w") as f:
    json.dump(config, f, indent=4)

# JSON file ko wapis read karna
with open("config.json", "r") as f:
    loaded = json.load(f)
    print(f"Model use ho raha hai: {loaded['model']}")



settings = {
    "learning_rate": 0.01,
    "batch_size": 32,
    "num_epochs": 50
}
with open("settings.json", "w") as file:
    json.dump(settings, file, indent=4)
with open("settings.json", "r") as file:
    loaded_settings = json.load(file)
    print(f"Learning Rate: {loaded_settings['learning_rate']}")
with open("settings.json", "a") as file:
    file.write("\n// This is a comment added to the JSON file.")
with open("settings.json", "r") as file:
    content = file.read()
    print("\nContent of settings.json:")
    print(content)