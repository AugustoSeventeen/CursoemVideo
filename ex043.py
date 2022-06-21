# IMC
import numpy as np

print('\033[33m=\033[m' * 40)
print(' ' * 12, '\033[32mFIND YOUR IMC\033[m')
print('\033[33m=\033[m' * 40)

b = float(input('What is your weight?: Kg: '))
a = float(input('How tall are you?: m: '))

imc = b / (a ** 2)
print('Your IMC is {:.1f}'.format(imc))
if imc < 18.5:
    print('\033[31mUnder weight\033[m')
elif 18.5 <= imc < 25:
    print('\033[32mIdeal weight\033[m')
elif 25 <= imc < 30:
    print('\033[33mOver weight\033[m')
elif 30 <= imc < 40:
    print('\033[37mObesity\033[m')
elif imc >= 40:
    print('\033[31mMorbid Obesity\033[m')
