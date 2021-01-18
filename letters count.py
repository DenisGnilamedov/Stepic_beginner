text = input() + ' '
counter = 0
match = text[0]

for symbol in text:
    if symbol != match:
        print(match, counter, end='', sep='')
        counter = 0
        match = symbol
    counter += 1

