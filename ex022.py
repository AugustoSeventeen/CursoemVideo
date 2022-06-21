# Read a name
f = input('Enter your name: ').strip()
s = f.split()
j = ''.join(s)
print('Your first name in capitalize letters is {} \n'
      'Your name in lowercase is {} \n'
      'Your name has {} letters \n'
      'Your first name is {} and has {} letters.'
      .format(f.upper(), f.lower(), len(j), s[0], len(s[0])))

