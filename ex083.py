# Parsing an expression
right = []
left = []
expression = str(input('Type an expression: '))
for symbol in expression:
    if symbol == '(':
        right.append('(')
    elif symbol == ')':
        left.append(')')
if right.count('(') == left.count(')'):
    print('\033[32mThis expression is correct!\033[m')
else:
    print('\033[31mThis expression is not correct\033[m')
