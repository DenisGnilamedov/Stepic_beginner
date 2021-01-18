def modify_list(l):
    for i in l[::-1]:
        if i % 2 == 0:
            l.remove(i)
            l.append(i // 2)
        elif i % 2 != 0:
            l.remove(i)
    l.reverse()


#lst = [int(i) for i in input().split()]
#print(modify_list(lst))
#print(lst)
