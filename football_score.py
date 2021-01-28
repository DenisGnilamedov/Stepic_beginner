n = int(input())
games = []
game = {}
for i in range(n):
    games.append(input().split(';'))
print(games)
for i in games:
    for j in i:
        game[[0]] = [1]
        game[[2]] = [3]
print(game)