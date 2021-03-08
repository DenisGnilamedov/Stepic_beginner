#_______________________________________________________________
'''cities = ['Austin', 'Tacoma', 'Topeka', 'Sacramento', 'Charlotte']
lst = [0 for i in range(7)]

dct = {city: lst for city in cities}'''

'''for city, lst in dct.items():
    print(city, lst)'''
#_______________________________________________________________
'''dct = {'Denis': 24}
for m,n in dct.items():
    print(m, n)'''
#_______________________________________________________________

result = {device: {key.lower():value for key, value in params.items()} for device, params in london_co.items()}

#_______________________________________________________________
'''lst = []
counter = 1
for i in range(3):
    tmp = []
    for j in range(3):
        tmp.append(counter)
        counter += 1
    lst.append(tmp)
print(lst)'''
#lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#_______________________________________________________________


def foo(i):
    return i**i/2+1


d = {i: foo(i) for i in range(1, 11)}
print(d)