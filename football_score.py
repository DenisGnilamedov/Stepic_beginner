# https://stepik.org/lesson/3380/step/1?unit=963
n = int(input())
games = [input().split(';') for i in range(n)]
temp = [(x[0], x[2]) for x in games]
team_list = []
for teams in temp:
    for team in teams:
        if team not in team_list:
            team_list.append(team)
teams = {team: [0, 0, 0, 0, 0] for team in team_list}
for team1, score1, team2, score2 in games:
    if int(score1) == int(score2):
        teams[team1][0] += 1
        teams[team2][0] += 1
        teams[team1][2] += 1
        teams[team2][2] += 1
        teams[team1][4] += 1
        teams[team2][4] += 1
    elif int(score1) > int(score2):
        teams[team1][0] += 1
        teams[team2][0] += 1
        teams[team1][1] += 1
        teams[team2][3] += 1
        teams[team1][4] += 3
    else:
        teams[team1][0] += 1
        teams[team2][0] += 1
        teams[team2][1] += 1
        teams[team1][3] += 1
        teams[team2][4] += 3

for team, team_stat in teams.items():
    print((team + ':'), *team_stat, end='\n')