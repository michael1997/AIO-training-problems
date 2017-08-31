file  = open("probein.txt", "r")
write_file = open("probeout.txt", "w")
row, column, water_row, water_column, lava_row, lava_column = file.readline().split()

blockade = False
if int(lava_row) + int(lava_column) == int(water_row) + int(water_column):
    blockade_sum = int(lava_row) + int(lava_column)
    blockade = True
    if lava_row < water_row:
        below = 'water'
    else:
        below = 'lava'
    
questions = int(file.readline())

for i in range(0, questions):
    question_row, question_column = file.readline().split()
    
    lava_value = abs(int(question_row)-int(lava_row)) + abs(int(question_column)-int(lava_column))
    water_value = abs(int(question_row)-int(water_row)) + abs(int(question_column)-int(water_column))

    if lava_value < water_value:
        write_file.write("LAVA\n")
    elif lava_value > water_value:
        write_file.write("WATER\n")
    else:
        if blockade:
            question_sum = int(question_row)+int(question_column)
            if below == 'water':
                if question_sum > blockade_sum:
                    write_file.write("WATER\n")
                else:
                    write_file.write("LAVA\n")
            else:
                if question_sum > blockade_sum:
                    write_file.write("LAVA\n")
                else:
                    write_file.write("WATER\n")
            
        else:
            write_file.write("MOUNTAINS\n")
        


file.close()
write_file.close()
