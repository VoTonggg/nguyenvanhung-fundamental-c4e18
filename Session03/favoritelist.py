favorite_things = ["death note","netflix","teaching"]

print("Hi there, here your favorite things so far")
print(*favorite_things, sep=', ')

one_more = input("Name one thing you want to add: ")
favorite_things.append(one_more)
print(*favorite_things, sep=', ')