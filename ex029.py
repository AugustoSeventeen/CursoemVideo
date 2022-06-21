# Read the car's velocity
v = float(input('What was your speed? : '))

m = (v - 80) * 7

if v > 80:
    print('You exceeded 80Km/h, you were {:.1f}Km/h, you need to pay R$:{:.2f} Reais' .format(v, m))
else:
    print('Congratulations! You were in the limit')
