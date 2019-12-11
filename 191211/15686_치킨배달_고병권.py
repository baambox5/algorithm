import sys
sys.stdin = open('chicken.txt', 'r')


def perm(k, s):
    global min_dist
    if k == M:
        sum_dist = 0
        for value in house.values():
            min_chicken = 100000
            for j in range(M):
                if min_chicken > value[order[j]]:
                    min_chicken = value[order[j]]
            sum_dist += min_chicken
            if sum_dist >= min_dist:
                break
        if sum_dist < min_dist:
            min_dist = sum_dist
    else:
        for i in range(s, len(chicken)):
            order[k] = i
            perm(k + 1, i + 1)


N, M = map(int, input().split())
arr = [input().split() for _ in range(N)]
chicken = []
house = {}
for i in range(N):
    for j in range(N):
        if arr[i][j] == '1':
            house[(i, j)] = []
        elif arr[i][j] == '2':
            chicken.append((i, j))
for x_h, y_h in house:
    for x_c, y_c in chicken:
        house[(x_h, y_h)] += [abs(x_h - x_c) + abs(y_h - y_c)]
order = [0] * M
min_dist = 100000
perm(0, 0)
print(min_dist)
