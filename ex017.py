# Calculate the hypotenuse
from math import pow, sqrt
print('='*10, 'FIND THE HYPOTENUSE!', '='*10)
o = float(input('Enter the Opposite Side: '))
a = float(input('Enter the Adjacent side: '))
h = (pow(a, 2)) + (pow(o, 2))
h1 = sqrt(h)
print('The Hypotenuse is: {:.2f}' .format(h1))









