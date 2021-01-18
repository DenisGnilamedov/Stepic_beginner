def update_dictionary(d, key, value):
    lst = []
    if key in d:
        d[key].append(value)
    elif 2*key in d:
        d[2*key].append(value)
    else:
        lst.append(value)
        d[2 * key] = lst


d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)                            # {2: [-1, -2, -3]}
'''d = {5: 100, 4: 5}
lst = []
if 2 in d:
        lst.append(d.get(2))
if 2 not in d:
    lst.append(d.get(2*4))
    if 2*4 not in d:
        d[2*4] = 444

print(lst)
print(d)
'''





