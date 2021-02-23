#https://stepik.org/lesson/3380/step/4?unit=963
n = int(input())
x, y = 0, 0
moves = [input().split(' ') for i in range(n)]

for direction, counter in moves:
    if direction == 'север':
        y += int(counter)
    elif direction == 'запад':
        x -= int(counter)
    elif direction == 'юг':
        y -= int(counter)
    elif direction == 'восток':
        x += int(counter)
print(x, y)