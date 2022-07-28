# finding the biggest parameter
from time import sleep


def line():
    print('\033[32m=\033[m' * 50)


def biggest(*num):
    line()
    count = biggest = 0
    print('\n\033[32mAnalyzing the numbers...\033[m')
    sleep(0.3)
    for value in num:
        print(f'\033[34m{value}\033[m', end=' ')
        sleep(0.3)
        if count == 0:
            biggest = value
        else:
            if biggest < value:
                biggest = value
        count += 1
    print(f'\n\033[33mWas informed {count} values.\033[m')
    print(f'\033[33mThe biggest value is\033[m \033[34m{biggest}\033[m.')


biggest(4, 27, 89, 44, 1, 34, 17)
biggest(4, 5, 45, 78, 3, 29)
biggest(18, 17, 19, 3)
