# Countdown
from time import sleep
print('\033[31m+-\033[m' * 30)
print(' ' * 15, '\033[33mCOUNTDOWN TO FIREWORK!!!\033[m')
print('\033[31m+-\033[m' * 30)
sleep(1)
print('Ready?...')
sleep(1)
for a in range(10, 0-1, -1):
    sleep(1)
    print(a)
print('FIRE!!!')
