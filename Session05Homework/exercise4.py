mature_rabbit = 2
not_mature = 0

months =  int(input("How many months has passed? "))

for i in range(months + 1):
    print("MONTH {0}: {1} pair(s) of rabbit".format(i, (mature_rabbit + not_mature) // 2))
    alter = not_mature
    not_mature = mature_rabbit
    mature_rabbit += alter

