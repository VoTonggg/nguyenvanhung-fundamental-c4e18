# person = ["Quy", 20, 0, "Vinh Phuc", 2, ["Manga", "Coding"], 3, 20]

#dictionary

person = {
    "name": "Quy",
    "age" : 20,
    "ex" : 0,
    "favs" : ["manga", "coding"]
}

print(person)

# name = person["favs"]
# print(name)

person["length"] = 20

# print(person)

# person["length"] = 10

# print(person)

# del person["length"]
# key = "age"
# if key in person:
#     print(person[key])
# else:
#     print("Not found")

# print(person)

# for k in person:
#     print(k,person[k])

# for value in person.values():
#     print(value)

for key, value in person.items():
    print(key, value)