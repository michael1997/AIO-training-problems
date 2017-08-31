file  = open("farmin.txt", "r")
plots = int(file.readline())
sizes = file.readline().split()
file.close()

left_index = 0
right_index = plots-1
area_left = int(sizes[left_index])
area_right = int(sizes[right_index])
fences = 0
while(left_index < right_index):
    if area_left > area_right:
        right_index = right_index - 1
        area_right = area_right + int(sizes[right_index])
        fences = fences + 1
        
    elif area_left < area_right:
        left_index = left_index + 1
        area_left = area_left + int(sizes[left_index])
        fences = fences + 1
        
    else:
        right_index = right_index - 1
        left_index = left_index + 1
        area_right = area_right + int(sizes[right_index])
        area_left = area_left + int(sizes[left_index])
    



file = open("farmout.txt", "w")
file.write(str(fences))
file.close()
