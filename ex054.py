# analysing the age of 7 people and saying who is overage and not yet.
from datetime import date
o = 0
u = 0
for x in range(1, 8):
    a = int(input('Which year you were born?: '))
    i = date.today().year - a
    if i < 18:
        u += 1
    else:
        o += 1
print('There are {} underage and {} overage!'.format(u, o))
