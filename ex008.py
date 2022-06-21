# Convert a meter unit to centimeters and millimeters
x = float(input('Enter your unit in Meters: '))
c = (x * 10) * 10
m = ((x * 10) * 10) * 10
f = x / 0.0254
f1 = f / 12
f2 = f - 12 * f1
f3 = f1 + f2

print('Centimeters: {} cm \nMillimeters: {} mm \nFeet and Inches: {:.1f} f&i' .format(c, m, f3))



