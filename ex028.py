# Guessing game
from random import choice
from time import sleep
print('=' * 10, 'GUESSING GAME', '=' * 10)
x = int(input('From 0 to 10, what number am I thinking now?: '))
y = range(0, 10)
z = choice(y)
print('PROCESSING...')
sleep(2)
if x == z:
    print('You got it!!!')
    print('=' * 10, 'END GAME', '=' * 10)
else:
    print('Bad luck, o thought in', z)
    print('=' * 10, 'GAME OVER :(', '=' * 10)

