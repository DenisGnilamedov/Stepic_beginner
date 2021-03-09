# https://stepik.org/lesson/3380/step/5?unit=963
stat = []
with open(r"C:\1\dataset_3380_5.txt", "r", encoding='utf-8') as lst:
    for i in lst:
        line = i.strip().split('\t')
        stat.append(line)
grades = {grade: [] for grade in range(1, 12)}
pupils = {pupil: [0, 0] for pupil in range(1, 12)}
for grade, pupil, height in stat:
    pupils[int(grade)][0] += 1
    pupils[int(grade)][1] += int(height)
for grade, pupil, height in stat:
    grades[int(grade)] = pupils[int(grade)][1]/pupils[int(grade)][0]
for grade in grades:
    if not (grades[grade]):
        grades[grade] = '-'

with open(r"C:\1\result.txt", "a") as ouf:
    for grade, mid in grades.items():
        ouf.write(str(grade) + ' ' + str(mid) + '\n')


#print(grade, mid, end='\n')



