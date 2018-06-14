yob = int(input("Your year of birth: "))

age = 2018 - yob

# print(age)

if age < 10:
    print("Baby")
elif age <= 18:
    print("Teenager")
elif age == 24:
    print("Lay chong thoi")
else:
    print("Not baby")

print("Bye")
