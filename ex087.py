# Matrix 3x3 2.0
matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pair_sum = sum_third = largest_value = 0
for row in range(0, 3):
    for column in range(0, 3):
        matrix[row][column] = int(input(f'Type the item [{row} {column}]: '))
        if matrix[row][column] % 2 == 0:
            pair_sum += matrix[row][column]
        if matrix[2][column]:
            sum_third += matrix[2][column]
        if matrix[1][0] > matrix[1][1] > matrix[1][2]:
            largest_value = matrix[1][0]
        elif matrix[1][1] > matrix[1][0] > matrix[1][2]:
            largest_value = matrix[1][1]
        else:
            largest_value = matrix[1][2]
for row in range(0, 3):
    for column in range(0, 3):
        print(f'\033[32m[\033[m{matrix[row][column]:^5}\033[32m]\033[m', end='')
    print()
print(f'The sum of pair number is: {pair_sum}')
print(f'The sum of values from third line is {sum_third}')
print(f'The largest value in second line is {largest_value}')
