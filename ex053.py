# If a phrase is a palindrome
print('=' * 10, '\033[36mPALINDROME FOUNDER\033[m', '=' * 10)
a = str(input('Type a frase: ')).strip().split()
b = ''.join(a).lower()
c = len(b)
x = ''
for d in range(c - 1, -1, -1):
    x += b[d]
if x == b:
    print('\033[32mThis phrase is a Palindrome!\033[m')
else:
    print('\033[31mThis phrase is not a Palindrome!\033[m')
