numb_bacterias = int(input("How many B bacterias are there? "))
time_period = int(input("How much time in minutes will we wait? "))

print("After {0} minutes, we would have {1} bacterias".format(time_period, numb_bacterias * ( 2 ** (time_period // 2))))