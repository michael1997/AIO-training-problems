file  = open("chairsin.txt", "r")
num, people, wet_people = file.readline().split()
num = int(num)
people = int(people)
wet_people = int(wet_people)

chairs = file.readline()
dry_people = people - wet_people

startptr = 0
endptr = 0
dry = 0
wet = 0
shortest = people

for i in chairs:
    startptr = startptr + 1
    if i == 'w':
        if valid(people, dry_people, wet, dry):
            
    elif i == 'd':
        if valid(people, dry_people, wet, dry) == False:
            dry = dry + 1
            while valid(people, dry_people, wet, dry):
                if chairs[endptr] == 'w':
                    wet = wet - 1
                else:
                    dry = dry - 1
                
                
        else:
            endptr = endptr + 1
            shortest = min(shortest, endptr-startptr)
    




file.close()


def valid(people, dry_people, wet, dry):
    if dry < dry_people:
        return False
    if wet + dry < people:
        return False
    return True
