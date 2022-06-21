# Show if a number is even or odd
x = int(input('Type a number: '))
n = x % 2

if n == 1:
    print('{} is odd!'.format(x))
else:
    print('{} is even!'.format(x))
