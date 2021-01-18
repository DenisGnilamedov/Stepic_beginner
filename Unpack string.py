# text = 'a3b4c2e10b1'
inf = open(r"C:\1\dataset_3363_2.txt", "r")
text = inf.readline() + 'c'
inf.close()
letter = ''
digit = ''
count = ''
result = ''
for i in text:
    if i >= 'A':
        if len(letter) > 0 and len(count) > 0:
            result += (letter * int(count))
        count = ''
        letter = ''
        letter += i
        continue
    if i < 'A':
        digit += i
        count += digit
        digit = ''
ouf = open(r"C:\1\res.txt", "w")
ouf.write(result)
ouf.close()


