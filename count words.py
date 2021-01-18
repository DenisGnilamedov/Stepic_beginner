text = open(r"C:\1\dataset_3363_3.txt").read().lower().strip().split()
d = {}
match = text[0]
counter = 0
word_answer = 'z'
counter_answer = 0
for word in text:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1
for word in d:
    if d[word] > counter_answer:
        word_answer = word
        counter_answer = d[word]
    if d[word] == counter_answer:
        if word < word_answer:
            word_answer = word
print(word_answer, counter_answer)
print(text)