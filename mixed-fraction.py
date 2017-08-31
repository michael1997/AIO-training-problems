file  = open("mixin.txt", "r")
num, den = file.readline().split()

file.close()

whole = int(num) // int(den)

fraction_num = int(num) % int(den)

file = open("mixout.txt", "w")

if fraction_num == 0:
    file.write(str(whole))
else:
    file.write(str(whole) + " " + str(fraction_num) + "/" + den)
file.close()
