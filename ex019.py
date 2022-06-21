# Draw a name
import random
print('=' * 10, 'NAME GIVEAWAY', '=' * 10)
a = (input('Enter the first name: '))
b = (input('Enter the second name: '))
c = (input('Enter the third name: '))
d = (input('Enter the fourth name: '))
p = [a, b, c, d]
print('The choose name is {}, congratulations!' .format(random.choice(p)))







