file  = open("artin.txt", "r")
num = int(file.readline())
found = False
hanging_blocks = []
max_height = 0
for i in range(0, num):
    time, width, height = file.readline().split()
    for j in hanging_blocks:
        if j[1] >= int(time):
            j[0] = j[0] + int(height)
            if j[0] > max_height:
                max_height = j[0]
            j[1] = int(time)+int(width)-1
            found = True
            break
    if found == False:
        hanging_blocks.append([int(height), int(time)+int(width)-1])
    found = False




file.close()


file = open("artout.txt", "w")
file.write(str(max_height))
file.close()
