# Analysing 2 numbers:
a = float(input('First number: '))
b = float(input('Second number: '))
if a > b:
    print('{} is bigger than {}!'.format(a, b))
elif a < b:
    print('{} is smaller than {}!'.format(a, b))
elif b > a:
    print('{} is bigger than {}!'.format(b, a))
elif b < a:
    print('{} is smaller than {}!'.format(b, a))
elif a == b:
    print('{} is equals {}!'.format(a, b))
