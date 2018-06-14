
for i in range(5):
    if i == 0 or i ==4:
        for j in range(23):
            if j == 5 or j== 11 or j == 16 or j == 17:
                print(" ", end='')
            else:
                print("*",end='')
        print()
    elif i == 1 or i == 3:
        for j in range(23):
            if j == 0 or j == 6 or j == 10 or j ==12 or j == 16 or j == 18:
                print("*",end='')
            else:
                print(" ",end='')
        print()
    else:
        for j in range(23):
            if j == 0 or j == 6 or j == 10 or j ==12 or j == 16 or j == 18 or j == 19 or j == 20 or j == 21 or j==22:
                print("*",end='')
            else:
                print(" ",end='')
        print()