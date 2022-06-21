# Choosing what to do with a number
a = int(input('Type a number: '))
b = int(input('Type a 2° number: '))
c = int(input('''[1] Add
[2] Multiply
[3] Bigger
[4] Other number
[5] Finish
: '''))
while c != 5:
    if c == 1:
        print('{} + {} = {}'.format(a, b, a + b))
        a = int(input('Type a number: '))
        b = int(input('Type a 2° number: '))
        c = int(input('''[1] Add
[2] Multiply
[3] Bigger
[4] Other number
[5] Finish
: '''))
    if c == 2:
        print('{} X {} = {}'.format(a, b, a * b))
        a = int(input('Type a number: '))
        b = int(input('Type a 2° number: '))
        c = int(input('''[1] Add
[2] Multiply
[3] Bigger
[4] Other number
[5] Finish
: '''))
    if c == 3 and a > b:
        print('{} is bigger than {}'.format(a, b))
        a = int(input('Type a number: '))
        b = int(input('Type a 2° number: '))
        c = int(input('''[1] Add
[2] Multiply
[3] Bigger
[4] Other number
[5] Finish
: '''))
    if c == 3 and a < b:
        print('{} is bigger than {}'.format(b, a))
        a = int(input('Type a number: '))
        b = int(input('Type a 2° number: '))
        c = int(input('''[1] Add
[2] Multiply
[3] Bigger
[4] Other number
[5] Finish
: '''))
    if c == 4:
        a = int(input('Type a number: '))
        b = int(input('Type a 2° number: '))
        c = int(input('''[1] Add
[2] Multiply
[3] Bigger
[4] Other number
[5] Finish
: '''))
print('See you later...')
