#  Break and Continue Statements in Python
#  while loop with break statement
i = 1
while i <= 10:
    if i == 5:
        break  # Exit the loop when i is 5
    print(i)
    i += 1
print("Loop ended with break statement at i =", i)
#  while loop with continue statement
j = 1
while j <= 10:
    if j == 5:
        j += 1
        continue  # Skip the rest of the loop when j is 5
    print(j)
    j += 1
print("Loop ended with continue statement at j =", j, "and skipped 5.")
#  for loop with break statement
for k in range(1, 11):
    if k == 5:
        break  # Exit the loop when k is 5
    print(k)
print("For loop ended with break statement.")
#  for loop with continue statement
for m in range(1, 11):
    if m == 5:
        continue  # Skip the rest of the loop when m is 5
    print(m)
print("For loop ended with continue statement.")
