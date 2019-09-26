import sys
sys.stdin = open('1799.txt', 'r')


def perm(k, count, visit, s, n):
    global max_count
    if k == n:
        if count > max_count:
            max_count = count
        return
    else:
        for i in range(s, p_len):
            if visit & (1 << i):
                continue
            if valid(k, i):
                order[k] = i
                perm(k + 1, count + 1, visit | (1 << i), i, n)


def valid(m, n):
    for x in range(p_len):
        if order[x]:
            if possible[order[x]][1] + m - possible[order[x]][0] == n or possible[order[x]][1] - m + possible[order[x]][0] == n:
                return 0
    else:
        return 1


N = int(input())
arr = [[0] * N for _ in range(N)]
possible = []
for i in range(N):
    arr[i] = input().split()
    for j in range(N):
        if arr[i][j] == '1':
            possible += [(i, j)]
max_count = 0
p_len = len(possible)
order = [0] * p_len
for j in range(p_len):
    perm(0, 0, 0, 0, j)
print(max_count)


def perm(k, count):
    global max_count
    if k == N:
        if count > max_count:
            max_count = count
        return
    else:
        for i in range(N):
            if arr[k][i] == '1' and valid(k, i):
                order[k][i] = 1
                count += 1
            perm(k + 1, count)


def valid(m, n):
    for x in range(m):
        for y in range(N):
            if order[x][y] and (y + m - x == n or y - m + x == n):
                return 0
    else:
        return 1


N = int(input())
arr = []
for _ in range(N):
    arr += [input().split()]
max_count = 0
order = [[0] * N for _ in range(N)]
perm(0, 0)
print(max_count)

