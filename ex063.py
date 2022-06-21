# Fibonacci sequence
print('\033[36m=\033[m' * 40)
print(' ' * 10, '\033[35mFIBONACCI SEQUENCE\033[m')
print('\033[36m=\033[m' * 40)
t = int(input("How many term's do you want?: "))
s = 1
f1 = 0
f2 = 1
f3 = f1 + f2
while s <= t:
    f3 = f2 + f1
    print('{}'.format(f3), end='')
    print(', ' if s < t else '.', end='')
    f1 = f2
    f2 = f3
    s += 1
