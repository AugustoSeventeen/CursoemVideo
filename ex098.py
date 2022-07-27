# counting with rules
from time import sleep


def line():
    print('\033[33m~\033[m' * 40)


def counter(s, a, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Counting from {s} to {a} by {p} by {p}')
    line()
    sleep(0.5)
    if s < a:
        count = s
        while count <= a:
            print(f'{count}', end=' ', flush=True)
            sleep(0.5)
            count += p
    else:
        count = s
        while count >= a:
            print(f'{count}', end=' ', flush=True)
            sleep(0.5)
            count -= p


counter(1, 10, 1)
counter(10, 0, 2)
line()
print('Now it is your time!')
start = int(input('Start: '))
end = int(input('End: '))
path = int(input('Path: '))
counter(start, end, path)
