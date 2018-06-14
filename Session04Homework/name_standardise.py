name = input("Your full name: ")

name = name.lower()

while ("  " in name):
    name = name.replace("  ", " ")
    
name = name.title()

print(name)

 