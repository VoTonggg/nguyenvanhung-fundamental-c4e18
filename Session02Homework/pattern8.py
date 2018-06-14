n = int(input("Enter a number: "))

for i in range(n):
    for j in range(1,n+1,1):
        print((j+i) % 2, end=' ')
    print()