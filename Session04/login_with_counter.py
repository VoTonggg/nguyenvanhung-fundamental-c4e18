print("Hi there, this is a superuser gateway")

count = 0

while True:
    username = input("Username: ")
    if username != "c4e":
        print("You are not superuser")
    else:
        password = input("Password: ")
        if password != "123":
            print("Password is incorrect")
        else:
            print("Welcome my friend!!")
            break
    count += 1
    if count == 3:
        print("You failed to log in 3 times, go away")
        break
    
    