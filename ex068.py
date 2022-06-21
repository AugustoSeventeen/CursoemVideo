# Even or odd game with computer
import random
from time import sleep
print('\033[35m=\033[m' * 40)
print(' ' * 10, '\033[36mEVEN OR ODD GAME\033[m')
print('\033[35m=\033[m' * 40)
cont = 0
while True:
    print('\033[36m=\033[m' * 60)
    c = random.choice(range(0, 11))
    p = int(input('Type a number: '))
    pc = str(input('Even or Odd? [E/O]: ')).strip().lower()
    print('Let me think...')
    sleep(1)
    n = p + c
    if n % 2 == 0 and pc in 'Ee':
        print(f'You choose {p} and I choose {c}, the sums is {n}, Even!, \033[32mYou Win\033[m')
    elif n % 2 == 1 and pc in 'Oo':
        print(f'You choose {p} and I choose {c}, the sums is {n} Odd!!, \033[32mYou Win\033[m')
    cont += 1
    if n % 2 == 0 and pc in 'Oo':
        print(f'You choose {p} and I choose {c}, the sum is {n}, Even!, \033[31mYou lose\033[m')
        break
    if n % 2 == 1 and pc in 'Ee':
        print(f'You choose {p} and I choose {c}, the sum is {n}, Odd!, \033[31mYou lose\033[m')
        break
print(f'You won {cont - 1} in a row!')
