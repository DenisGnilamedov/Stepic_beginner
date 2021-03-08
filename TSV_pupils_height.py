# https://stepik.org/lesson/3380/step/5?unit=963
stat = []
with open(r"C:\1\test.txt", "r", encoding='utf-8') as lst:
    for i in lst:
        line = i.strip().split('\t')
        stat.append(line)
stat.sort(key=lambda x: int(x[0]))
grades = list(range(1, 12))
grades_dict = {grade: [] for grade in range(1, 12)}
for grade, name, height in stat:
    if grade == i:
        j += 1
        new_stat = {grade: j for grade in grades}
        print(new_stat)
print(grades_dict)
'''
temp_stat = [int(line[0]) for line in stat]
i = 0

sum_height = 0
for grade in grades:
    if grade in temp_stat:
        if grade not in new_stat:
            new_stat.append(grade)
        else:
            continue
    elif grade not in temp_stat:
        new_stat.append("-")'''


#print(stat)
#print(grades)
#print(temp_stat)







