file = open("dishin.txt", "r")
numbers = int(file.readline())

mini = 100000000000000
maxi = 0
total = 0
for i in range(0, numbers):
    num = int(file.readline())
    if num < mini:
        mini = num
    elif num > mini:
        maxi = num
    total = total + num
avg = int(total // numbers)


file = open("dishout.txt", "w")
file.write(str(mini) + " " + str(maxi) + " " + str(avg))
file.close()
