# 1. Kharchon ko store karne ke liye dictionary
expenses = {}

print("--- Welcome to Smart Expense Tracker ---")
print("Type 'done' when you are finished adding expenses.\n")

total_budget = int(input("Enter your total monthly budget in PKR: "))
while True:
    # 2. User se category aur price lena
    category = input("Enter category (e.g., Food, Rent, Fun) or 'done': ").lower()
   
    if category == 'done':
        break
    try:
        price = int(input(f"How much did you spend on {category}? "))
    except ValueError:
        print("Please enter a valid number for price.")
        continue

    # 3. Wahi logic jo aapne character counter mein lagaya tha!
    if category in expenses:
        expenses[category] += price
    else:
        expenses[category] = price

for remove in expenses:
    if remove == input("Enter the category you want to remove from the report (or type 'none' to skip): ").lower():
        del expenses[remove]
        try: 
            print(f"{remove.capitalize()} category removed from the report.")
        except KeyError:
            print("Category not found in the report.")
        break

# Item Counter: Dictionary mein sirf paise jama na karein, ye bhi hisab rakhein ke "Food" ki category mein kitni bar entries hui hain.
item_count = {}
for category in expenses:
    if category in item_count:
        item_count[category] += 1
    else:
        item_count[category] = 1
print("\n--- Expense Category Counts ---")
for category, count in item_count.items():
    print(f"{category.capitalize()}: {count} entries")

# 4. Aakhir mein report dikhana
print("\n--- Your Monthly Expense Report ---")
total_spend = 0

# loop use karke dictionary se data nikalna
for item, amount in expenses.items():
    print(f"- {item.capitalize()}: {amount} PKR")
    total_spend += amount

print(f"\nTotal Money Spent: {total_spend} PKR")
print(f"Remaining Budget: {total_budget - total_spend} PKR")
if total_spend > total_budget:
    print("You have exceeded your budget! Consider cutting down on expenses.")


