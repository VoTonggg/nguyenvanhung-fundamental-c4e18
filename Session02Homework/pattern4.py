n = int(input("Enter the number of 1's and 0's: "))

for i in range(n // 2):
        print("1 0 ", end='')
if (n % 2 == 1 ):
    print("1")
