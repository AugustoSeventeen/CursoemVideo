#Sin, Cos and Tan
from math import sin, cos, tan, radians
n = float(input('Enter a angle: '))
print('The Sine of {} is {:.2f} \n The cosine is {:.2f} \n And tangent is {:.2f}' .format(n, sin(radians(n)),
                                                                                     cos(radians(n)),
                                                                                        tan(radians(n))))


