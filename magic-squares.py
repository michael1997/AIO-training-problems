file  = open("magicin.txt", "r")
a, b, c = file.readline().split()
file.close()

line1 = a + " " + b + " " + str(20-int(a)-int(b))
line2 = c + " " + str(20-int(c)-int(b)) + " " + b
line3 = str(20-int(c)-int(a)) + " " + c + " " + a
file = open("magicout.txt", "w")
file.write(line1 + "\n" + line2 + "\n" + line3)
file.close()
