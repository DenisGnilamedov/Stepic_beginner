n = int(input())
a = n % 10
b = n % 5 == 0
c = n % 100
if (a == 0) or b:
    print(n, 'программистов')
elif a == 1 and n != 11 and n != 111:
    print(n, 'программист')
elif 11 <= c <= 19:
    print(n, 'программистов')
elif a == 2 or a == 3 or a == 4:
    print(n, 'программиста')
elif a == 6 or a == 7 or a == 8 or a == 9:
    print(n, 'программистов')


'''n = int(input())
if (n % 10 == 1 and n%100 != 11):
    print(n, 'программист')
elif (n % 10 in [2, 3, 4] and not n % 100 in [12, 13, 14] ):
    print(n, 'программиста')
else:
    print(n, 'программистов')'''


#1 программист , 2 3 4 программиста , 5 6 7 8 9 10 программистов