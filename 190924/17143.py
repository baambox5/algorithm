import sys
sys.stdin = open('17143.txt', 'r')


def move(n, x, y, d, s):
    if d == 2:
        if x + s > R:
            s += x - R
            x = R
            d = 1
            move(n, x, y, d, s)
            return
        else:
            x += s
            s = 0
            if x == R:
                d = 1
    elif d == 1:
        if x - s < 1:
            s += 1 - x
            x = 1
            d = 2
            move(n, x, y, d, s)
            return
        else:
            x -= s
            s = 0
            if x == 1:
                d = 2
    elif d == 3:
        if y + s > C:
            s += y - C
            y = C
            d = 4
            move(n, x, y, d, s)
            return
        else:
            y += s
            s = 0
            if y == C:
                d = 4
    else:
        if y - s < 1:
            s += 1 - y
            y = 1
            d = 3
            move(n, x, y, d, s)
            return
        else:
            y -= s
            s = 0
            if y == 1:
                d = 3
    if not s:
        shark[n][1] = x
        shark[n][2] = y
        shark[n][4] = d


R, C, M = map(int, input().split())
shark = [[1] for _ in range(M)]
for i in range(M):
    shark[i] += list(map(int, input().split()))
arr = [[0] * (C + 1) for _ in range(R + 1)]
for i in range(M):
    arr[shark[i][1]][shark[i][2]] = i + 1
res = 0
for k in range(1, C + 1):
    for i in range(1, R + 1):
        if arr[i][k] and shark[arr[i][k] - 1][0]:
            res += shark[arr[i][k] - 1][5]
            shark[arr[i][k] - 1][0] = 0
            arr[i][k] = 0
            break
    for i in range(M):
        if shark[i][0]:
            move(i, shark[i][1], shark[i][2], shark[i][4], shark[i][3])
    arr = [[0] * (C + 1) for _ in range(R + 1)]
    for i in range(M):
        if not shark[i][0]:
            continue
        x = shark[i][1]
        y = shark[i][2]
        if arr[x][y]:
            if shark[i][5] > shark[arr[x][y] - 1][5]:
                shark[arr[x][y] - 1][0] = 0
                arr[x][y] = i + 1
            else:
                shark[i][0] = 0
        else:
            arr[x][y] = i + 1
print(res)
