favs = ["deadth note", "netflix", "teaching"]

print("Hi there, here your favorite things so far")
for index, item in enumerate(favs):
    print("{0}. {1}".format(index+1, item))

position = int(input("Position you want to upade? "))
replace_fav = input("Your replacing favorite? ")

favs[position-1] = replace_fav

for index, item in enumerate(favs):
    print("{0}. {1}".format(index+1, item))