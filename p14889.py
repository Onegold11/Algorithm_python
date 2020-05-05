import sys


def backtracking(num, team, table, i=0):
    global min_score

    if i == num / 2:
        team1_score, team2_score = score(team, table)
        diff = abs(team1_score-team2_score)

        if diff < min_score:
            min_score = diff
    else:
        for people in range(num):
            team.append(people)

            if promising(team, people):
                backtracking(num, team, table, i + 1)

            team.pop()


def promising(team, people):
    if len(team) == 1:
        return True
    elif people < team[-2]:
        return False
    elif people in team[:-1]:
        return False
    else:
        return True


def score(team, table):
    team1 = team
    team2 = []

    num = len(team) * 2
    for i in range(num):
        if i not in team1:
            team2.append(i)

    team1_score = 0
    for i in team1:
        for j in team1:
            if i != j:
                team1_score = team1_score + table[i][j]

    team2_score = 0
    for i in team2:
        for j in team2:
            if i != j:
                team2_score = team2_score + table[i][j]

    return team1_score, team2_score


num = int(input())
s_table = []
team = []
min_score = 100

for _ in range(num):
    s_table.append(list(map(int, sys.stdin.readline().split())))

backtracking(num, team, s_table)
print(min_score)