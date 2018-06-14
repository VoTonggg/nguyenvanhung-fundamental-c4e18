prices = {
    "banana" : 4,
    "apple" : 2,
    "orange" : 1.5,
    "pear" : 3
}

stock = {
    "banana" : 6,
    "apple" : 0,
    "orange" : 32,
    "pear" : 15
}

for key in prices:
    print(key)
    print("price:", prices[key])
    print("stock:", stock[key])
    print()

total = 0
for key in prices:
    price = prices[key] * stock[key]
    print("Sold {0} {1}, you got {2} dollars".format(stock[key], key, price))
    total += price

print("Sold out everything and you got {0} dollars".format(total))