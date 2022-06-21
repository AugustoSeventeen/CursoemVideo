# Rock paper scissor
from random import choices
print('\033[31m+-\033[m' * 30)
print(' ' * 17, 'ROCK PAPER SCISSOR')
print('\033[31m+-\033[m' * 30)
print(' ')
print('\033[33mChoose one!\033[m')

x = int(input('1 = ROCK\n2 = PAPER\n3 = SCISSOR\nI choose: '))
y = ['ROCK', 'PAPER', 'SCISSOR']
z = choices(y, k=1)


if x == 1 and z == ['ROCK']:
    print('Computer: Rock!')
    print('Draw!')
elif x == 1 and z == ['PAPER']:
    print('Computer: Paper!')
    print('I win!')
elif x == 1 and z == ['SCISSOR']:
    print('Computer: Scissor!')
    print('You win!')
elif x == 2 and z == ['ROCK']:
    print('Computer: Rock!')
    print('You win!')
elif x == 2 and z == ['PAPER']:
    print('Computer: Paper!')
    print('Draw!')
elif x == 2 and z == ['SCISSOR']:
    print('Computer: Scissor!')
    print('I win!')
elif x == 3 and z == ['ROCK']:
    print('Computer: Rock!')
    print('I win!')
elif x == 3 and z == ['PAPER']:
    print('Computer: Paper!')
    print('You win!')
elif x == 3 and z == ['SCISSOR']:
    print('Computer: Scissor!')
    print('Draw!')

