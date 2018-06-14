# this = ["I", "am", "not", "a", "crook"]
# that = ["I", "am", "not", "a", "crook"]

# print("Test 1: {0}".format(this is that))

# that = this
# print("Test 2: {0}".format(this is that))

def checkPalindrome(inputString):
    is_palindrome = True
    for i in range(len(inputString)):
        if inputString[i] != inputString[n-1-i]:
            is_palindrome = False
    return is_palindrome
    
inputString = "aabaa"
print(checkPalindrome(inputString))                   