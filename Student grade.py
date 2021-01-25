a = b = c = d = 0
with open(r"C:\1\dataset_3363_4.txt", "r", encoding='utf-8') as lst:
    for line in lst:
        with open(r"C:\1\solution.txt", "a") as ouf:
            line = line.strip().split(';')
            a += int(line[1])
            b += int(line[2])
            c += int(line[3])
            d += 1
            mid = ((int(line[1])+int(line[2])+int(line[3])) /3)
            ouf.write(str(mid))
            ouf.write('\n')
        mid_sum1 = a / d
        mid_sum2 = b / d
        mid_sum3 = c / d
    with open(r"C:\1\solution.txt", "a") as ouf:
        ouf.write(str(mid_sum1) + ' ')
        ouf.write(str(mid_sum2) + ' ')
        ouf.write(str(mid_sum3))


