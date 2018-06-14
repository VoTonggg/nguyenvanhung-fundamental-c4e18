item_list = ["T-Shirt", "Sweater"]

order= input("Welcome to our shop, what do you want (C, R, U, D)? ")

if order == "R" or order == "r":
    print("Our items: ", end="")
    print(*item_list, sep=', ')
elif order == "C" or order == "c":
    new_item = input("Enter new item: ")
    item_list.append(new_item)
    print("Our items: ", end="")
    print(*item_list, sep=', ')
elif order == "U" or order == "u":
    position = int(input("Update position? "))
    if position > len(item_list):
        print("Please input a valid position")
        print("Your item list has only",len(item_list),"items")
        position = int(input("Update position? "))
    new_item = input("New item? ")
    item_list[position-1] = new_item
    print("Our items: ", end="")
    print(*item_list, sep=', ')
elif order == "D" or order == "d":
    position = int(input("Delete position"))
    if position > len(item_list):
        print("Please input a valid position")
        print("Your item list has only",len(item_list),"items")
        position = int(input("Delete position? "))
    del item_list[position-1]
    print("Our items: ", end="")
    print(*item_list, sep=', ')

else:
    print("Do not know what you want to do!!!")
