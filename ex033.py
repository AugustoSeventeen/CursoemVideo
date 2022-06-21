# Biggest and smallest number
n1 = int(input('First number: '))
n2 = int(input('Second number'))
n3 = int(input('Third number'))
# Checking what is the biggest one
if n1 > n2 and n1 > n3:
    print('{} is the biggest number!'.format(n1))
if n2 > n1 and n2 > n3:
    print('{} is the biggest number!'.format(n2))
if n3 > n1 and n3 > n2:
    print('{} is the biggest number!'.format(n3))
# Checking what is the smallest one
if n1 < n2 and n1 < n3:
    print('{} is the smallest number!'.format(n1))
if n2 < n1 and n2 < n3:
    print('{} is the smallest number!'.format(n2))
if n3 < n1 and n3 < n2:
    print('{} is the smallest number!'.format(n3))
