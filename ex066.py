# Show how many numbers was typed and the sum, if person type 999, stop.
s = cont = 0
while True:
    a = int(input('\033[32mType a number [999] To stop: \033[m'))
    if a == 999:
        break
    s += a
    cont += 1
print(f'You typed {cont} numbers and sum is {s}')
