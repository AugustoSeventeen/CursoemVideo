# matrix 3x3
matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# Feeding the matrix with datas:
for row in range(0, 3):
    for column in range(0, 3):
        matrix[row][column] = int(input(f'Type a item [{row} {column}]: '))
# Making the matrix:
for row in range(0, 3):
    for column in range(0, 3):
        print(f'\033[32m[\033[m{matrix[row][column]:^5}\033[32m]\033[m', end='')
    print()
