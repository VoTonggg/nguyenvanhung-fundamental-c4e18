# food1 = "Salad Nga"
# food2 = "Chocolate"
# food3 = "So"
# food4 = "Mi Tom"
# food5 = "Pho"

#list #array

#Create
menu = ["Salad Nga", "Chocolate", "So", "Mi Tom", "Pho" ]

#seperator
#Read
# print(*menu, sep=', ')

# print(len(menu))

# menu.append("Banh Muot")
# print(*menu, sep=', ')
# print(len(menu))

# first_item = menu[-1]
# print(first_item)

# for i in range(5):
#     print(i+1, ". ", menu[i], sep='')

# for i in range(len(menu)):
#     print("{0}. {1}".format(i+1, menu[i]))

# print("* "*20)

for index, item in enumerate(menu):
    print("{0}. {1}".format(index+1, item))

print("* "*20)

# for item in menu:
#     print(item)

menu[2] = "Cua"

print(*menu, sep=", ")
