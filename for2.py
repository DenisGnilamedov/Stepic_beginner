a = int(input())
b = int(input())
s = 0
u = 0
for g in range(a, b+1):
    if g % 3 == 0:
        s += g
        u += 1
sa = s / u
print(sa)
#считает количество чисел кратных 3 и их ср арифметическое