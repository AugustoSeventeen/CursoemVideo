# Car rent
d = int(input('For how many days did you use the car? '))
k = float(input('How many kilometers did you drive? '))
d1 = d * 60
k1 = k * 0.15
print('You used the car for {} days and drive for {} Km so you need to pay R$:{} Reais.' .format(d, k, (d1 + k1)))


