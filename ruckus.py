file = open("ruckusin.txt", "r")
N, L, K, M = file.readline().split
N = int(N)
L = int(L)
K = int(K)
M = int(M)

connected = {}
#if connected[child] = 0 => no hands
#if connected[child] = 1 => 1 or 2 hands
#no need to store having 2 hands

line_index = {}
#stores the line index the child is in 

lines = []
#array of arrays containg [end1, end2, size, valid]

cycles = []
#array of sizes of cycles

for i in range(0, L):
    a, b = file.readline().split()
    a = int(a)
    b = int(b)
    if connected.get(a) == None:
        #no line or cycle previously
        if line_index.get(b) == None:
            #partner isn't in a line (nb can't be in a cycle)
            lines.append([a, b, 2, True])
            #both children have 1 hand now
            connected[a] = 1
            connected[b] = 1
            #add them both to map of index in lines
            line_index[a] = len(lines) - 1
            line_index[b] = len(lines) - 1
            #move to next pair
            continue
        else:
            #partner is already in a chain
            #get the chain index
            index = line_index[b]
            if lines[index][0] == b:
                #set the new end of the chain
                lines[index][0] = a
            elif lines[index][1] == b:
                #set the new end of the chain
                lines[index][1] = a
            else:
                print("error")
            #increase the len of the chain
            lines[index][2] = lines[index][2] + 1
            #add the index to the dictionary
            line_index[a] = index
            connected[a] = 1
    else:
        #already part of a chain
        if line_index.get(b) != None:
            #both have chains
            if line_index.get(b) == line_index.get(a):
                #same chain => cycle now
                cycles.append(lines[line_index.get(a)][2])
                lines[line_index.get(a)][3] = False
            else:
                #different chains
                lines[line_index.get(a)][3] = False
                
                
                
            
            
            
            
            
    
