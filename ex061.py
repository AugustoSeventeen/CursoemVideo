# Make an arithmetic progression with while
f = int(input('\033[36mEnter the first element: \033[m'))
r = int(input('\033[36mEnter the reason: \033[m'))
c = 1
p = f + r
while c <= 10:
    print('\033[33m{}\033[m'.format(f), end='')
    print('\033[33m, \033[m' if c < 10 else '\033[33m.\033[m', end='')
    f += r
    c += 1
