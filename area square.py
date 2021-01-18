fig = str(input())
if fig == 'треугольник':
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a + b + c)/2
    S = (p*(p-a)*(p-b)*(p-c))**0.5
    print(S)
elif fig == 'прямоугольник':
    a = float(input())
    b = float(input())
    print(a * b)
elif fig == 'круг':
    r = float(input())
    S = 3.14 * r**2
    print(S)
else:
    print('Unknown figure type')







