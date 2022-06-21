# making an AP questioning how many term's person wants
from time import sleep
f = int(input('\033[32mWhat is the first term?: \033[m'))
r = int(input('\033[32mWhat is the reason?: \033[m'))
c = 0
t = 0
a = 10
while a != 0:
    t += a
    while c <= t:
        print('{}'.format(f), end='')
        print(', ' if c < t else '.', end='')
        f += r
        c += 1
    a = int(input("\nHow many mores term's you want? \n[0] To exit: "))
if a == 0:
    print('Processing...')
    sleep(1)
    print('Finished.')
