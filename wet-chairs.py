file  = open("probein.txt", "r")
num, people, wet_people = file.readline().split()
chairs = file.readline()
dry_people = int(people) - int(wet_people)

dry = 0
wet = 0
for i in chairs:
    if i == 'w':
        wet = wet + 1
    if i == 'd':
        dry = dry + 1



file.close()
