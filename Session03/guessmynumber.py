from random import randint

numb = randint(0,100)

count = 0
loop = True
while loop:
    if count >= 7:
        print("You loserrrrrrrrrrrrrrrrr")
        loop = False
    else:
        n = int(input("Guess my number (1-100)? "))
        if (n == numb):
            print("Bingo")
            loop = False
        elif (n < numb):
            print("Too small")
        else:
            print("A little too large")

    count += 1

