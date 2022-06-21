# Show a factorial number
a = int(input('Type a number: '))
factorial = 1
print('{}! ='.format(a), end=' ')
while a > 0:
    print('{}'.format(a), end=' ')
    print('x' if a > 1 else '=', end=' ')
    factorial *= a
    a -= 1
print('{}'.format(factorial))
