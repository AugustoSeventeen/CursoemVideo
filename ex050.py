# Sum of 6 integers numbers, just the pair numbers
s = 0
for a in range(1, 7):
    b = int(input('Type a number: '))
    if b % 2 == 0:
        s += b
print('The of just pair numbers is', s)
