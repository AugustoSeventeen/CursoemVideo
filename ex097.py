# adaptive lines
def write(text):
    size = len(text) + 4
    print('\033[34m~\033[m' * size)
    print(f'  \033[33m{text}\033[m')
    print('\033[34m~\033[m' * size)


write('Computer test')
write('Augusto Vinicius')
