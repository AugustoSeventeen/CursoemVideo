# Read numbers, calculate de average, the biggest and lowest.
b = 's'
a = sum = cont = biggest = lowest = 0
while b not in 'Nn':
    a = int(input('\033[32mType a number: \033[m'))
    b = str(input('\033[36mContinue? [S/N]\033[m'))
    sum += a
    cont += 1
    if cont == 1:
        biggest = lowest = a
    else:
        if a > biggest:
            biggest = a
        if a < lowest:
            lowest = a
print('You typed {} number, the average is {}, the biggest is {} and the lowest is {}'.format(cont, sum / cont, biggest,
                                                                                              lowest))
