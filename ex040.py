# Average of a student
import numpy as np
a = float(input('First note: '))
b = float(input('Second note: '))
m = (a + b) / 2

if m < 5:
    print('\033[31mDISAPPROVED!\033[m')
elif 5 < m <= 7:
    print('\033[33mRECOVERY!\033[33m')
elif 7 < m:
    print('\033[32mAPPROVED!\033[m')
