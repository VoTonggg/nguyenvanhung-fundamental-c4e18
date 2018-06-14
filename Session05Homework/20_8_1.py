string = input("Enter the string: ")

letters = {}

for letter in string:
    if letter == " ":
        continue
    if letter in letters:
        letters[letter] += 1
    else:
        letters[letter] = 1
letter_items = list(letters.items())
letter_items.sort()


for i in range(len(letter_items)):
    print(*letter_items[i])