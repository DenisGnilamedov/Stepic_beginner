#https://stepik.org/lesson/3380/step/3?unit=963
d = int(input())
correct_words = set()
for word in range(d):
    correct_words.add(input().lower())
error_words = set()
l = int(input())
for string in range(l):
    for word in input().lower().split():
        error_words.add(word)
print(*error_words.difference(correct_words), sep='\n')
