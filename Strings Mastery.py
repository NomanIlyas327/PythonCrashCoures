# # Important Methods (Safayi ke Tools):

# # .strip(): Faltu spaces ya \n (new lines) ko khatam karta hai.

# # .split(","): Jaisa aapne kal kiya, comma se data ko list mein badalta hai.

# # .replace("old", "new"): Kisi galat word ko sahi karne ke liye.

# # .lower() / .upper(): Taake "Ali" aur "ali" mein koi farq na rahe (ML models ke liye dono alag ho sakte hain).


# Python Task: Ek string banayen data = "  Lahore, 40C, Sunny  ".

# Iski faltu spaces khatam karein (strip).

# Isay commas se alag karein (split).

# City ka naam Capital mein convert karein.


data = "  Lahore, 40C, Sunny  "

parts = data.strip().split(",")
print(parts)

city = parts[0].strip().upper()
temp = parts[1].strip()
weather = parts[2].strip()

print(f"City : {city}")
print(f"Temprature : {temp}")
print(f"Weather : {weather}")

new_list = [city , temp , weather]
print(f"Clean List : {new_list}")


