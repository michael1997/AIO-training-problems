file = open("countin.txt", "r")
numbers = int(file.readline())
file.close()

file = open("countout.txt", "w")
for i in range(1, numbers+1):
    file.write(str(i) + "\n")
file.close()
