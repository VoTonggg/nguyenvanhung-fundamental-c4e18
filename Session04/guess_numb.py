print("Guess your number game")

print("Now think of a number from 0 to 100, then press 'prime.py Enter'")
input()

# print("All you have to do is have to answer to my guess")
# print("'c' if my guess is 'C'orrect")
# print("'s' if my guess is 'S'aller than your number")
# print("'l' if my guess is 'L'arger than your number")

print("""
All you have to do is have to anwser to my guess
'c' if my guess is 'C'orrect
's' if my guess is 'S'maller than your number
'l' if my guess is 'L'arger than your number
""")

low = 0
high = 100

while True:
    mid = (low + high) // 2
    ans = input("Is {0} your number? ".format(mid)).lower()
    if (ans == 's'):
        low = mid
    elif (ans == 'l'):
        high = mid
    else:
        print("I knew it!!!")
        break
