# Main chahta hun aap in sab cheezon ko mila kar aik "Inventory Management System" ka chota sa script likhen.

# Task:

# Ek Dictionary banayein inventory = {"apple": 50, "banana": 20, "orange": 30}.

# Ek Function banayein update_stock(item, quantity).

# Agar item inventory mein hai, to uski quantity add kar dein.

# Agar nahi hai, to naya item add karein.

# Ek Loop chalayein jo poori inventory ko print kare: f"Hamare paas {item} ke {count} pieces hain".

# Set ka istemal: Ek list banayein jisme duplicates hon ["apple", "apple", "mango"] aur usse unique items nikaal kar inventory mein check karein.


inventory = {"apple": 50, "banana": 20, "orange": 30}

def update_stock():
    # 1. Item ka naam lein
    item = input("Enter the name of Item : ").lower().strip()
    quantity = int(input(f"Enter the quantity for {item}: "))
    
    # 2. Logic: Agar pehle se hai to jama karo, warna naya dalo
    if item in inventory:
        inventory[item] += quantity
        print(f"--- {item.capitalize()} ka stock update ho gaya! ---")
    else:
        inventory[item] = quantity # Dictionary mein append nahi hota, direct assign hota hai
        print(f"--- {item.capitalize()} naya add kiya gaya! ---")

# Function ko call karein
update_stock()

# 3. Inventory Print karne ka Loop (Separate)
print("\n--- Current Inventory Status ---")
for item, count in inventory.items():
    print(f"Hamare paas {item} ke {count} pieces hain")

# 4. Set ka istemal (Unique list se check karna)
check_list = ["apple", "apple", "mango", "banana", "mango"]
unique_items = set(check_list) # Duplicate khatam: {'apple', 'mango', 'banana'}

print("\n--- Checking items from checklist ---")
for x in unique_items:
    if x in inventory:
        print(f"{x.capitalize()} stock mein maujood hai.")
    else:
        print(f"{x.capitalize()} stock mein NAHI hai.")