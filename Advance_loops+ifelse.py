# Level 1: Nested Conditions (Logic Check)
# Problem: "The Smart ATM"
# Ek program likhein jo user se balance aur withdrawal_amount le.

# Agar withdrawal amount balance se zyada hai, toh print karein "Inadequate Funds".

# Agar withdrawal amount 10,000 se zyada hai, toh print karein "Daily Limit Exceeded".

# Warna, balance mein se amount minus karein aur print karein "Transaction Successful! Remaining: [balance]".

balance = int(input("Enter the balance amount: "))
withdrawal_amount = int(input("Enter the withdrawal amount: "))
if withdrawal_amount > balance:
    print("Inadequate Funds")
elif withdrawal_amount > 10000:
    print("Daily Limit Exceeded")
else:
    remaining_balance = balance - withdrawal_amount
    print(f"Transaction Successful! Remaining: {remaining_balance}")



# Level 2: Loop + Logic (The FizzBuzz Classic)
# Ye interview ka sabse mashhoor sawal hai.
# Problem: 1 se 20 tak numbers print karein, lekin:

# Agar number 3 se divide hota ho, toh number ki jagah "Fizz" likhein.

# Agar number 5 se divide hota ho, toh number ki jagah "Buzz" likhein.

# Agar dono (3 aur 5) se hota ho, toh "FizzBuzz" likhein.

def fizzBuzz(n):
    result = []
    for i in range(1,n+1):
        if i % 3 == 0 and  i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

print(fizzBuzz(20))
        


# Level 3: While Loop (The Guessing Game)
# Problem:

# Ek variable set karein secret_number = 7.

# User se baar baar input lein jab tak wo sahi number guess na kar le.

# Agar user ka guess galat ho, toh batayein ke guess "Too High" hai ya "Too Low".

# Jab user sahi guess kar le, toh loop ruk jaye aur print ho "You Won!".

# [Image showing the process of a while loop in a guessing game, comparing user input to a secret key]


secret_number = 7

def start_guessing_game():
    while True: # Ye loop chalta rahega jab tak user sahi guess na karle
        user_guess = int(input("Guess the Number: ")) # Input loop ke andar hai
        
        if user_guess > secret_number:
            print("Too High! Try again.")
        elif user_guess < secret_number:
            print("Too Low! Try again.")
        else:
            print("You Won! 🏆")
            break # Sahi jawab milne par loop rok do

# Function ko chalane ke liye call karein
start_guessing_game()


# Level 4: List + Loop (Advanced Logic)
# Problem: "Find the Peak"
# Aapke paas aik list hai: heights = [1, 3, 7, 8, 5,10, 2].
# Loop chala kar wo pehla number dhoondain jo apne aglay (next) number se bada ho. (Yani jahan se "pahaar" neechay utarna shuru ho raha hai).

# Hint: range(len(heights) - 1) use karein taaki i+1 error na de.


heights = [1, 3, 7, 8, 5, 10, 2]
for i in range(len(heights) - 1):
    if heights[i] > heights[i+1]:
        print("Peak Found at " ,heights[i])
        break


# Ek Choti si Practice (For you to solve now):
# Aapke paas ye list hai: scores = [45, 78, 32, 90, 55, 10, 88]
# Ek program likhein jo:

# List par loop chalaye.

# Agar score 80 se zyada hai, toh loop ko break kar de (Ruk jaye).

# Sirf wo scores print kare jo 40 se baray hon.

scores = [45, 78, 32, 90, 55, 10, 88]
print(f"Given Scores : {scores}" )
for x in scores:
    if x > 80:
        break
    if x > 40:
        print(x)
    