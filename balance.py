file = open("balancein.txt", "r")
num = int(file.readline())
stacks = file.readline().split()
file.close()

for i in range(0, num):
    stacks[i] = int(stacks[i])

moves = 0

left_index = 0
right_index = num - 1



while left_index < right_index:
    if stacks[left_index] > stacks[right_index]:
        right_index = right_index - 1
        stacks[right_index] = stacks[right_index+1] + stacks[right_index]
        moves = moves + 1
        right_stack = stacks[right_index]
        #print("moving to", right_index)

    elif stacks[left_index] < stacks[right_index]:
        left_index = left_index + 1
        stacks[left_index] = stacks[left_index-1] + stacks[left_index]
        #print(str(stacks[left_index]))
        moves = moves + 1
        
        #print("moving to", left_index)

    else:
        right_index = right_index - 1
        left_index = left_index + 1
        #print("balanced")
file = open("balanceout.txt", "w")
file.write(str(moves))
file.close()
