# Calculating the employee's salary
a = float(input('What is your salary? R$:'))
if a >= 1250:
    b = (a * 10) / 100
    print('You will get an increase of 10% \nYour new salary will be R$:{:.2f}'.format(b + a))
else:
    c = (a * 15) / 100
    print('You will get an increase of 15% \nYour new salary will be R$:{:.2f}'.format(c + a))
