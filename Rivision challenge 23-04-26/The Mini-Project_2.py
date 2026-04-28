# Mini-Project: Smart Warehouse Manager
# Sochein aap ek warehouse ke manager hain. Aapko ek aisa system banana hai jo inventory ko track kare, expiry check kare, aur low stock ka alert de.

# Is Project mein hum ye sab use karenge:
# Dictionary: Product ki details (price, quantity) rakhne ke liye.

# Lists: Items ki categories store karne ke liye.

# Functions: Add, Update, aur View karne ke liye.

# Loops & Conditions: Stock khatam hone par alert dene ke liye.

# Phase 1: Structure Taiyar Karein
# Sabse pehle humein data chahiye. Ek dictionary banayein jahan har item ki key uska naam ho aur value ek aur dictionary ho.

# Python
# # Initial Inventory
# inventory = {
#     "Milk": {"price": 150, "quantity": 10, "category": "Dairy"},
#     "Bread": {"price": 80, "quantity": 2, "category": "Bakery"},
#     "Eggs": {"price": 300, "quantity": 15, "category": "Dairy"}
# }
# Phase 2: Logic Building (Your Tasks)
# Main aapko 3 Challenges deta hoon. Inhein ek ek karke solve karein:

# Task 1: The Alert System (Loops & Conditions)
# Ek function banayein check_low_stock().

# Ye inventory par loop chalaye.

# Agar kisi item ki quantity 5 se kam ho, toh print kare: "ALERT: [Item Name] is low on stock! Only [Qty] left."

# Task 2: Smart Billing (Functions & Parameters)
# Ek function banayein generate_bill(item_name, bought_qty).

# Check karein ke kya wo item inventory mein hai?

# Check karein ke kya itni quantity maujood hai?

# Agar sab theek hai, toh total price calculate karein aur inventory mein se quantity minus kar dein.

# Task 3: Category Filter (List Comprehension)
# Ek function banayein get_items_by_category(cat_name).

# Ye sirf us category ke items ki list return kare jo user ne mangi hai.


inventory = {
     "Milk": {"price": 150, "quantity": 10, "category": "Dairy"},
     "Bread": {"price": 80, "quantity": 2, "category": "Bakery"},
     "Eggs": {"price": 300, "quantity": 15, "category": "Dairy"}
 }


def check_low_stock():
    for item in inventory:
        if inventory[item]["quantity"] < 5:
            print(f"ALERT: {item} is low on stock! Only {inventory[item]['quantity']} left.")

check_low_stock()

def generate_bill(item_name, bought_qty):
    if item_name in inventory:
        if inventory[item_name]["quantity"] >= bought_qty:
            total_price = inventory[item_name]["price"] * bought_qty
            inventory[item_name]["quantity"] -= bought_qty
            print(f"{inventory[item_name]['quantity']} {item_name} left in stock.")
            print(f"Bill for {bought_qty} {item_name}: {total_price} Rs.")
        else:
            print(f"Sorry, only {inventory[item_name]['quantity']} {item_name} left in stock.")

generate_bill("Milk", 3)


def show_category(cat_name):
    items_in_category = [item for item in inventory if inventory[item]["category"] == cat_name]
    return items_in_category
print(show_category(input("Enter category name: ")))