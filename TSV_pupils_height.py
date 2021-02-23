# https://stepik.org/lesson/3380/step/5?unit=963
stat = []
with open(r"C:\1\dataset_3380_5.txt", "r", encoding='utf-8') as lst:
    for i in lst:
        line = i.strip().split('\t')
        stat.append(line)
stat.sort(key=lambda x: int(x[0]))
new_stat = {}

'''cnt = 1
counter = 0
sum_height = 0
for line in stat:
    while int(line[0]) == cnt:
        counter += 1
        sum_height += int(line[2])
        if int(line[0]) > cnt:
            mid_height = sum_height/counter
            new_stat[cnt] = mid_height
            cnt += 1
            counter = 0
            sum_height = 0
        continue'''
print(stat)




# with open(r"C:\1\solution2.txt", "a") as ouf: