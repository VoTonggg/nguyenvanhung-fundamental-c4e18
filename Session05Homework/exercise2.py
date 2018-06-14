numbers = [1, 6, 8, 1, 2, 1, 5, 6]
numb = int(input("Enter a number? "))

### without using count() function
# count = 0
# for item in numbers:
#     if item == numb:
#         count += 1
# print("{0} appears {1} in my list".format(numb, count))

### with using count() function
print("{0} appears {1} in my list".format(numb, numbers.count(numb)))
