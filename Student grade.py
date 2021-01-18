with open(r"C:\1\dataset_3363_4.txt", encoding='utf-8') as lst:
    for grad in lst:
        grade = grad.strip().split(';')
print(lst)

'''for i in range(len(lst)):
            for j in range(len(lst[i])):
                print(lst[i][1], end=' ')
            print()'''


#x = (int(grade[1]) + int(grade[2]) + int(grade[3])) / 3
#        print(x)