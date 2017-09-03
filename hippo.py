file = open("hippoin.txt", "r")
daisies = int(file.readline())

hippo1 = int(file.readline())
hippo2 = int(file.readline())
hippo3 = int(file.readline())

zone1 = hippo1 - 1
zone2 = hippo2-hippo1-1
zone3 = hippo3-hippo2-1
zone4 = daisies-hippo3

# can only save 2 zones and 2 and 3 can't both be saved

answer = max(zone1+zone2, zone1+zone3, zone1+zone4, zone2+zone4, zone3+zone4)
file = open("hippoout.txt", "w")
file.write(str(answer))
file.close()


    

