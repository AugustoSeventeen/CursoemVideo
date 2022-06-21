# Sum of all odd numbers multiples of 3 between 1 and 500
x = 0 # accumulator
y = 1 # counter
for n in range(0, 501, 3):
    a = n % 2
    if a == 1:
        x += n
        y += 1
print('The sum of {} items is {} '.format(y, x))
