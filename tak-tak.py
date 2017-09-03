file = open("taktakin.txt", "r")
apples = int(file.readline())
file.close()

moons = 0
while apples % 11 != 1:
    apples = apples*2
    moons = moons + 1

file = open("taktakout.txt", "w")
file.write(str(moons) + " " + str(apples))
file.close()
