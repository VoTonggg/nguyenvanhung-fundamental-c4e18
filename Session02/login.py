import getpass

username = input("Username: ")
password = getpass.getpass("Password: ")

# if username == "stefannguyen" and password == "123456789":
#     print("Welcome, Stefan Nguyen")
# elif username != "stefannguyen":
#     print("Wrong username or password")
# elif password != "123456789":
#     print("Wrong password ")
# else:
#     print("No such user, go away")

if username == "stefannguyen":
    if password == "123456789":
        print("welcome")
    else:
        print("Wrong password")
else:
    print("No such user. Go away")