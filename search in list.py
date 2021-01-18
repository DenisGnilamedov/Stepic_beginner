lst = [int(i) for i in input().split()]
x = int(input())
if x not in lst:
    print('Отсутствует')
for index, i in enumerate(lst):
    if i == x:
        print(index, end=' ')

