# Reading datas
from time import sleep
ca = gm = wt = 0
while True:
    print('\033[33m=\033[m' * 60)
    a = int(input('What is your age?: '))
    if a > 18:
        ca += 1
    g = ' '
    while g not in 'mfMF':
        g = str(input('What is your genre? [M/F]: ')).strip().lower()
    if g in 'Mm':
        gm += 1
    if g in 'Ff' and a < 20:
        wt += 1
    q = ' '
    while q not in 'YyNn':
        q = str(input('Continue? [Y/N]')).strip().lower()
    if q in 'nN':
        break
print('Processing...')
sleep(1)
print(f'There are {ca} people over 18 years old, {gm} men and {wt} women under 20 years.')
