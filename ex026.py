# Read a message and show how many times letter 'a' is show, where it is...
x = str(input('Type a phrase: ')).strip().split()
y = ''.join(x).lower()
print("There are {} letters 'a'" .format(y.count('a')))
print("The first letter 'a' is the {}° letter." .format(y.find('a') + 1))
print("The latest letter 'a' is the {}° letter." .format(y.rfind('a') + 1))
