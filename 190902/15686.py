import sys
sys.stdin = open('15686.txt', 'r')


def backtrack(k, s):
    global min_dist
    if k == M:
        house_dist = [100] * len(house)
        for i in range(M):
            for j in range(len(house)):
                row = chicken[order[i]][0] - house[j][0]
                if row < 0:
                    row = - row
                column = chicken[order[i]][1] - house[j][1]
                if column < 0:
                    column = - column
                if house_dist[j] > row + column:
                    house_dist[j] = row + column
        sum_dist = 0
        for i in range(len(house)):
            sum_dist += house_dist[i]
        if min_dist > sum_dist:
            min_dist = sum_dist
    else:
        for i in range(s, len(chicken)):
            order[k] = i
            backtrack(k + 1, i + 1)


N, M = map(int, input().split())
arr = []
house = []
chicken = []
order = [0] * M
min_dist = 10000
for i in range(N):
    arr += [input().split()]
    for j in range(N):
        if arr[i][j] == '2':
            chicken += [(i, j)]
        elif arr[i][j] == '1':
            house += [(i, j)]
house_dist = [100] * len(house)
backtrack(0, 0)
print(min_dist)
