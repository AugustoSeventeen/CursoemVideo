# 4 players playing with dice
from time import sleep
from random import randint
from operator import itemgetter
game = dict()
print('\033[33mRated Values:\033[m')
sleep(1)
game['Player 1'] = randint(1, 6)
game['Player 2'] = randint(1, 6)
game['Player 3'] = randint(1, 6)
game['Player 4'] = randint(1, 6)
ranking = list()
for k, v in game.items():
    print(f'The \033[34m{k}\033[m got the value \033[32m{v}\033[m')
    sleep(1)
ranking = sorted(game.items(), key=itemgetter(1), reverse=True)
print('=' * 20, 'Rank')
for item, v in enumerate(ranking):
    print(f'{item+1}° place: {v[0]} with {v[1]}')
    sleep(1)
