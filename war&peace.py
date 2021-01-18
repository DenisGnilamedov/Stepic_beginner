text = input().lower().split()
s = set(text)
for word in s:
    print(word, text.count(word))

