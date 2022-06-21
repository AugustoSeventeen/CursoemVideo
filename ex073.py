# Brasileirão table
a = ('Palmeiras', 'Corinthians', 'Athlético - PR', 'Athlético - MG', 'Internacional', 'Fluminense', 'Botafogo',
     'Santos', 'São Paulo', 'Bragantino', 'Avai', 'Athlético - GO', 'Ceará', 'Flamengo', 'Coritiba', 'América - MG',
     'Goiás', 'Cuiabá', 'Fortaleza', 'Juventude')
print(f'Brasileirão Table is {a}')
print('\033[33m=\033[m' * 60)
print(f'The five first is {a[0:6]}')
print('\033[33m=\033[m' * 60)
print(f'The last four is {a[-4:]}')
print('\033[33m=\033[m' * 60)
print(f'Teams in alphabetical order {sorted(a)}')
print('\033[33m=\033[m' * 60)
print(f'Chapecoense is in table')
