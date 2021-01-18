n = int(input())
a = n % 4 == 0
b = n % 100 != 0
c = n % 400 == 0
if a and (b or c):
    print('Високосный')
else:
    print('Обычный')
