lst = [int(i) for i in input().split()]


if len(lst) == 1:
    print(lst[0])

else:
    for index in range(len(lst)):
        print(lst[index - 1] + lst[(index + 1) % len(lst)], end=' ')
