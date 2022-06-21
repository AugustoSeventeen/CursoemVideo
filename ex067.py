# Do a Multiplication Table
print('\033[35m=\033[m' * 40)
print(' ' * 9, '\033[36mMULTIPLICATION TABLE\033[m')
print('\033[35m=\033[m' * 40)
while True:
    a = int(input('\033[36mType a number: \033[m'))
    if a < 0:
        break
    for x in range(1, 11):
        print(f'\033[32m{a}\033[m X \033[35m{x}\033[m = \033[33m{a * x}\033[m')
