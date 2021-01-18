r = int
while r:
    a = int(input())
    if a < 10:
        continue
    if a > 100:
        break
    print(a)

#выводить только числа в диапазоне 10 > a > 100/ Больше 100 - прерываем, меньше 10 не выводим.