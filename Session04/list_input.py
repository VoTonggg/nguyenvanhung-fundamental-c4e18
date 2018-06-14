scores = input("Nhap diem vao, ngan cach bang dau cach: ")

score_list_str = scores.strip().split(" ")


score_list_int = []

for item in score_list_str:
    score_list_int.append(int(item))

got_sorted = True

for i in range(len(score_list_int)-1):
    if score_list_int[i] > score_list_int[i+1]:
        got_sorted = False
        break

if got_sorted:
    print("Your sequence is already sorted")
else:
    print("Your sequence is not sorted")
    sorted_list = []
    while True:
        min_numb = min(score_list_int)
        sorted_list.append(min_numb)
        score_list_int.remove(min_numb)

        if len(score_list_int) == 0:
            break
    print("Sorted list is : ")
    print(*sorted_list)

print(*score_list_str)

