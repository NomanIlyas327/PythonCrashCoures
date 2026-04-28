# Level 1: Basic (Parameters & Return)
# Ek function banayein calculator(a, b, operation).

# Agar operation "add" ho toh dono ko jama karein.

# Agar "multiply" ho toh zarb (multiply) karein.

# Function result return kare.

def calculate(a, b):
    operand = input("Enter the Operand : ")
    if operand == "+" :
       return (a+b)
    if operand == "*":
       return (a*b)
    
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print(calculate(a , b))


# Level 2: Scope Logic (Intermediate)
# Neeche diye gaye code ko dekhein aur batayein ke print(a) aur print(b) ka output kya hoga (code chalaye baghair sochein):
# a = 100

# def test_scope():
#     a = 50
#     b = 20
#     print("Inside:", a)


# test_scope()
# print("Outside a:", a)
# # print("Outside b:", b) # Is line ka kya banay ga?


# Level 3: Pro (The Shopping Cart)
# Ek global list banayein cart = [].
# Do functions banayein:

# add_item(item_name): Jo cart mein item add kare (global use karte hue).

# show_cart(): Jo cart ke saare items print kare aur sath ye bhi bataye ke total kitne items hain.

cart = [] # Global List

def add_item():
    global cart # Technicaly append ke liye zaroori nahi, magar likhna bura bhi nahi
    while True:
        name = input("Enter item name (or type 'done' to finish): ")
        if name.lower() == "done":
            break
        cart.append(name)
        print(f"Added: {name}")

def show_cart():
    print("\n--- Your Shopping Cart ---")
    for index, item in enumerate(cart, 1): # Indexing ke saath print karna pro lagta hai
        print(f"{index}. {item}")
    print(f"Total Items: {len(cart)}")

def remove_item():
    remove_item = input("Enter the item name to remove: ")
    try:
      while remove_item in cart:
        cart.remove(remove_item)
        print(f"Removed: {remove_item}")
    except ValueError:
        print(f"{remove_item} not found in cart.")

def clear_cart():
    cart.clear()
    print("Cart cleared!")

      

# Calling the functions
add_item()
show_cart()
remove_item()
show_cart()
clear_cart()
show_cart()