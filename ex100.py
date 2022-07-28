# drawing and adding
from random import randint
from time import sleep


def draw_num(num):
    for v in range(0, 5):
        n = randint(1, 10)
        num.append(n)


numbers = list()
draw_num(numbers)


def add_pair(num):
    for i, v in enumerate(numbers):
        if v % 2 == 0:
            num.append(v)


pair_numbers = list()
add_pair(pair_numbers)
sum_pair = sum(pair_numbers)
print(f'\033[34mDrawing 5 numbers from list:\033[m', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.', end='')
sleep(1)
print(f' \033[33m{numbers}\033[m \033[32mReady!!!\033[m')
print(f'\033[35mAdding the pair values from {numbers} we have:\033[m \033[34m{sum_pair}\033[m')
