# lst = sorted([int(i) for i in input().split()])
lst = ['0', '0', '0', '2', '3', '3', '4', '4', '8']
t = ''
counter = 0

for value in lst:
    counter += 1
    if value != t:
        t = value
        counter = 1
        continue

    if counter == 2:
        print(value, end=' ')

