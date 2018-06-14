teencode_dictionary = {
    "hc" : "học tập",
    "ngta" : "người ta",
    "any" : "anh người yêu",
    "eny" : "em người yêu",
    "ng" : "người"
}

while True:
    for key in teencode_dictionary:
        print(key, end='\t')
    print()

    code = input("Your code: ")
    print("*"*20)

    if code in teencode_dictionary:
        print("Code:", code)
        print("Translation:", teencode_dictionary[code])
    else:
        answer = input("Not found, do you want to contribue this word? (Y/N) ").lower()
        if answer == "y":
            translation = input("Enter your translation: ")
            teencode_dictionary[code] = translation
            print("Updated")
        else: 
            print("Bye")
            break
    print("*"*20)
    for key in teencode_dictionary:
        print(key, end='\t')
    print()
        