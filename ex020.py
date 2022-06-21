# Choose the order of presentation
from random import sample
a = input('Enter the first name: ')
b = input('Enter the second name: ')
c = input('Enter the third name: ')
d = input('Enter the fourth name: ')
e = [a, b, c, d]
print('The order of presentation is:', sample(e, k=4))














