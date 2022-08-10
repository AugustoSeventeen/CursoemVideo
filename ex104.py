# Read just number.


def readint(msg):
    ok = False
    value = 0
    while True:
        number = str(input(msg))
        if number.isnumeric():
            value = int(number)
            ok = True
        else:
            print(f'\033[31mError! Type just numbers.\033[m')
        if ok:
            break
    return value


# main program
number = readint('Type a number: ')
print(f'You typed the number {number}')
