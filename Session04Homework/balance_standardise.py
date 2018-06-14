numb = input("Enter your balance: ")

numb_list = list(numb)

updated_balance = []

while True:
    if numb_list[0] == "0":
        del numb_list[0]
    else:
        break

if len(numb_list) % 3 == 0:
    for i in range(len(numb_list)):
        if i % 3 == 2 and i != len(numb_list)-1:
            updated_balance.append(numb_list[i])
            updated_balance.append(",")
        else:
            updated_balance.append(numb_list[i])
elif len(numb_list) % 3 == 1:
    for i in range(len(numb_list)):
        if i % 3 == 0 and i != len(numb_list)-1:
            updated_balance.append(numb_list[i])
            updated_balance.append(",")
        else:
            updated_balance.append(numb_list[i])
else:
    for i in range(len(numb_list)):
        if i % 3 == 1 and i != len(numb_list)-1:
            updated_balance.append(numb_list[i])
            updated_balance.append(",")
        else:
            updated_balance.append(numb_list[i])

   
print("".join(updated_balance))
