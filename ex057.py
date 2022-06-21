# Just accept M or F
a = str(input('What is your genre? [M/F]: ')).strip().lower()[0]
if a not in 'FfMm':
    print('\033[31mInvalid answer, please try again!\033[m')
    while a not in 'MmFf':
         a = str(input('What is your genre? [M/F]: ')).strip().lower()[0]
         if a not in 'MmFf':
            print('\033[31mInvalid answer, please try again!\033[m')
print('\033[32mThank you!\033[m')
