'''
n = int(input(''))
if (-15) < n <= 12:
    print('True')
elif 14 < n < 17:
    print('True')
elif 19 <= n:
    print('True')
else:
    print('False')
'''

n = int(input(''))
a = (-15) < n <= 12
b = 14 < n < 17
c = 19 <= n
print(a or b or c)

