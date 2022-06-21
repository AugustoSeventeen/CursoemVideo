# Reading Vowels
words = ('Gate', 'School', 'Bus', 'Tree', 'Time', 'Portuguese', 'Battery', 'Drones', 'Mug', 'Criticized', 'Wall')
for word in words:
    print(f'\nIn word \033[36m{word}\033[m we have ', end=' ')
    for letter in word:
        if letter.lower() in 'aeiou':
            print(f'\033[36m{letter}\033[m', end=' ')
