number_list = [10,2,-5,4,6 ,9, 10, -8, -9]
# sorted_list = []
# while True:
#     min_numb = min(number_list)
#     sorted_list.append(min_numb)
#     number_list.remove(min_numb)

#     if len(number_list) == 0:
#         break

# print(sorted_list)

while True:
    is_sorted = True
    for i in range(len(number_list)-1):
        if (number_list[i] > number_list[i+1]):
            number_list[i], number_list[i+1] = number_list[i+1], number_list[i]
            is_sorted = False
    if is_sorted:
        break


print(number_list)


