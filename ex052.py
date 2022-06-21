# Prime number
print('\033[33m=\033[m' * 40)
print(' ' * 13, '\033[34mPRIME NUMBER\033[m')
print('\033[33m=\033[m' * 40)
a = int(input('Type a number to see if it is a Prime Number: '))
b = 0
for c in range(1, a + 1):
    if a % c == 0:
        print('\033[31m{}'.format(c), end=', ')
        b += 1
    else:
        print('\033[32m{}'.format(c), end=', ')
if b == 2:
    print('\n\033[32m{} is a Prime Number!\033[m'.format(a))
else:
    print('\n\033[31m{} is not a Prime Number!\033[m'.format(a))
