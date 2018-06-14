from random import choice, randint

word_list = ["champion", "meticulous", "hexagon", "capuchino", "latte"]
word = choice(word_list)

chars = list(word)

chars_random = []

# for i in range(length):
#     numb = randint(0, len(chars)-1)
#     chars_random.append(chars[numb])
#     del chars[numb]

while len(chars) > 0:
    letter_random = choice(chars)
    chars_random.append(letter_random)
    chars.remove(letter_random)

print(*chars_random, sep=' ')
answer = input("Your answer: (You ONLY have 1 chance) ")

if answer == word:
    print("Hura")
else:
    print(";(")