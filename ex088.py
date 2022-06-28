# Guess lottery game
from time import sleep
from random import sample
print(f'=' * 40)
print(f' ' * 14, 'LOTTERY GAME')
print(f'=' * 40)
times = int(input(f'How many games do you want me to draw?: '))
values = range(0, 61)
counter = 1
print('Values is...')
sleep(1)
for games in range(0, times):
    print(f'Value {counter}: {sorted(sample(values, k=6))}')
    counter += 1
    sleep(1)
