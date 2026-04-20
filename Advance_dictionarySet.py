user = {"name": "Ali", "age": 25, "city": "Lahore"}

# 1. Access karna
print(user["name"]) # Output: Ali

# 2. Naya data add karna ya purana update karna
user["email"] = "ali@example.com"
user["age"] = 26 

# 3. Safe Access (Agar key na ho toh error nahi aata)
print(user.get("phone", "Not Found"))



numbers = {1, 2, 3, 4, 4, 2}
print(numbers) # Output: {1, 2, 3, 4} (Duplicates khud hi khatam!)

# 1. Add karna
numbers.add(5)

# 2. Remove karna
numbers.remove(3)

# 3. Membership test (Bohat kaam aata hai)
print(2 in numbers) # Output: True



A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union (Dono ke saare items)
print(A | B) # {1, 2, 3, 4, 5, 6}

# Intersection (Jo dono mein common hon)
print(A & B) # {3, 4}

# Difference (Jo A mein hon magar B mein na hon)
print(A - B) # {1, 2}


# Task 1 (Dictionary):
# Ek dictionary banayein stock = {"apples": 50, "bananas": 100, "oranges": 80}.

# bananas ki quantity update karke 120 kar dein.

# Ismein ek naya fruit "grapes": 40 add karein.

# .pop() use karke apples ko nikal dein.

stock = {"apples": 50, "bananas": 100, "oranges": 80}

stock["bananas"] = 120
stock["Grapes"] = 40
stock.pop("apples")
print(stock)


# Task 2 (Set - Duplicate Remover):
# Aapke paas aik list hai jis mein duplicate names hain:
# raw_names = ["Ali", "Sara", "Ali", "Zain", "Sara", "Dua"]
# Aik line mein is list se duplicates khatam karke ek nayi list banayein.
# (Hint: List ko set mein badlein, phir wapas list mein).

raw_names = ["Ali", "Sara", "Ali", "Zain", "Sara", "Dua"]
unique_raw_names = set(raw_names)
print(unique_raw_names)
raw_names = list(unique_raw_names)
print(raw_names)

# Task 3 (Dictionary - Word Counter):
# Aik string hai text = "python is fun and python is easy".
# Ek dictionary banayein jo ye count kare ke har word kitni dafa aaya hai.
# (Hint: Pehle .split() karein, phir loop chala kar check karein agar word dictionary mein hai toh +1 karein, warna 1 set karein).


word_count = {}
text = "python is fun and python is easy"
words = text.split()
print(words)
for word in words:
    if word in word_count:
        word_count[word] = word_count[word] + 1
    else:
        word_count[word] = 1
print(word_count)



# # Dictionary Comprehension (Mapping)
# Iska basic formula ye hai:
# {key: value for item in iterable if condition}


marks = {"ali": 45, "sara": 85, "zain": 30, "dua": 92}
passed_students = {name.upper(): score for name, score in marks.items() if score > 50}
print(passed_students)

#  Set Comprehension (Unique Transformation)
# Set comprehension tab use hoti hai jab aapko output mein sirf unique values chahiye hon aur saath hi kuch logic bhi apply karna ho.

sentence = "python is fun and python is powerful"
word_lenght = {len(wordss) for wordss in sentence.split()}
print(word_lenght)



# The Data Transformation Task:
# Aapke paas aik list hai: employees = [("Ali", 50000), ("Sara", 75000), ("Zain", 40000), ("Dua", 90000)]

# Goal: Ek Dictionary Comprehension likhein jo:

# Sirf un employees ko uthaye jinki salary 45000 se zyada hai.

# Key employee ka Naam ho.

# Value unki salary ho jisme 10% Bonus add kiya gaya ho.

# Checklist for you:

# [ ] Dictionary comprehension use karni hai {}.

# [ ] .items() ya list unpacking use karni hai.

# [ ] if condition lagani hai.

# [ ] Math operation (salary * 1.10) apply karna hai.


employees = [("Ali", 50000), ("Sara", 75000), ("Zain", 40000), ("Dua", 90000)]
updated_employees = {Name: salary * 1.10 for Name , salary in employees if salary > 45000}
print(updated_employees)