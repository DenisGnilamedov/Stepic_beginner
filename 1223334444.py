n = int(input())
s = []
for i in range(1, n+1):
    if len(s) >= n:
        break
    s += [i] * i
print(*s[:n], end=' ')
