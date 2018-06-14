number = int(input("Enter a number: "))

loop = True
for i in range(2,number):
    if number % i == 0:
        loop = False
        break

if loop == False:
    print(number, "is not a prime number")
else:
    print(number, "is a prime number")

