size_list = [5, 7, 300, 90, 24, 50, 75]

print("Hello, my name is Hiep and these are my ship sizes")
print(*size_list, sep=', ')

biggest = max(size_list)

print("Now my biggest sheep has size", biggest, "Lets shear it")

position = size_list.index(biggest)
size_list[position] = 8
print("After shearing, here is my flock")
print(*size_list, sep=', ')

n = int(input("How many months has passed ?"))

for i in range(1,n+1):
    print("MONTH", i, ":")
    print("One month has passed, now here is my flock")
    for j in range(len(size_list)):
        size_list[j] += 50

    print(*size_list, sep=', ')
    biggest = max(size_list)
    print("Now my biggest sheep has size",biggest,"lets shear it")
    if i < n:
        position = size_list.index(biggest)
        size_list[position] = 8
        print("After shearing, here is my flock")
        print(*size_list, sep=', ')

print("My flock has size in total:", sum(size_list))
print("I would get", sum(size_list), "* 2$ =", sum(size_list)*2)

        

