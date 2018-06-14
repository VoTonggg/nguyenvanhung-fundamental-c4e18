number_list = [1,4,5,2,7,32,7,1,3,6]

while True:
    is_sorted = True
    for i in range(len(number_list)-1):
        if (number_list[i] > number_list[i+1]):
            number_list[i], number_list[i+1] = number_list[i+1], number_list[i]
            is_sorted = False
    if is_sorted:
        break


print(number_list)