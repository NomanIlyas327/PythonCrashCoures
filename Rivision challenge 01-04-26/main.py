with open("Rivision challenge 01-04-26/prices.txt", "r") as file:
    content = file.read()
    print("File ka data ye raha:")
    print(content)

content_int = list(map(int, content.split()))
print("File ka data integer mein convert kar diya:")
print(content_int)
sum_of_prices = sum(content_int)
print("Total sum of prices:", sum_of_prices)
sum_of_prices_str = str(sum_of_prices)
with open("Rivision challenge 01-04-26/total_price.txt", "w") as file:
    file.write(sum_of_prices_str)
    print("Total price written to file.")   