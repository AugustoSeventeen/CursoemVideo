# Showing the biggest and lowest weight
biggest = 0
lowest = 0
for c in range(1, 6):
    a = float(input('{}° What is your weight?: '.format(c)))
    if c == 1:
        biggest = a
        lowest = a
    else:
        if a > biggest:
            biggest = a
        if a < lowest:
            lowest = a
print('The biggest one is {}Kg, and the lowest one is {}Kg!'.format(biggest, lowest))
