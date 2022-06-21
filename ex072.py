# Writing a number in full
a = ('Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve',
     'Thirteen', 'Fifteen', 'Fourteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen', 'Twenty')
while True:
    b = int(input('Type a number from 0 till 20 to know it in full: '))
    while b not in range(0, 21):
        b = int(input('Invalid answer!, Type a number from 0 till 20 to know it in full: '))
    print(f'{b} in full is {a[b]}')
    q = str(input('Continue? [Y/N]: ')).strip().lower()[0]
    if q in 'Nn':
        break
