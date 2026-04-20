dictionary = {"Bread": 2.5, "Milk": 1.5, "Eggs": 3.0, "Cheese": 4.0, "Apples": 0.5}
cart = []
total_bill = 0

for item, price in dictionary.items():
    print(f"{item}: {price}")
    

while True:
    item = input("Enter the item you want to buy (or 'done' to finish): ").capitalize()
    if item == 'Done':
        break


    if item in dictionary:
        cart.append(item)
        total_bill += dictionary[item]
        print(f"{item} added to cart. Current total: {total_bill}")
    else:        
        print("Item not found. Please try again.")

print(f"\nTotal bill: {total_bill}")
   
    
# 1. Dictionary (Day 5)
items = {"Apple": 100, "Banana": 50, "Orange": 80}

# 2. Lists (Day 3)
cart = []
total_bill = 0

print("--- Welcome to ML Store ---")
for item, price in items.items(): # Day 6 (Loops)
    print(f"{item}: Rs.{price}")

# 3. User Input & Logic
while True:
    choice = input("\nItem ka naam likhein (ya 'exit' likhein): ").capitalize()
    if choice == 'Exit':
        break
    
    if choice in items:
        cart.append(choice)
        total_bill += items[choice]
        print(f"{choice} cart mein add ho gaya!")
    else:
        print("Sorry, ye item nahi hai.")

print(f"\nAapka total bill: Rs.{total_bill}")
print(f"Items kharide: {cart}")

with open ("sensor_data.txt", "w") as file:
    print("5 dino ka temperature enter krain:")
    for i in range(5):
        temp = input(f"Day {i+1}: ")
        file.write(temp + "\n")

temps_lists = []
with open ("sensor_data.txt", "r") as file:
    print("\n5 dino ke temperature:")
    for line in file:
        t = float(line.strip())
        temps_lists.append(t)

# avg_temp = sum(temps_lists) / len(temps_lists)
print(f"\nAnalsys report:")
# print(f"\nAverage temperature: {avg_temp}")
print(f"Maximum temperature: {max(temps_lists)}")