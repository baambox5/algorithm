import sys
sys.stdin = open('dessert.txt', 'r')


def dessert(x, y, c, f, s, k):
    global max_count
    if x == ox and y == oy:
        if c > max_count:
            max_count = c
        return
    elif kind[arr[x][y]]:
        return
    else:
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < N:
            if k == 0:
                kind[arr[x][y]] = 1
                dessert(nx, ny, c + 1, f + 1, s, k)
                kind[arr[x][y]] = 0
                if f:
                    dessert(x, y, c, f, s, k + 1)
            elif k == 1:
                kind[arr[x][y]] = 1
                dessert(nx, ny, c + 1, f, s + 1, k)
                kind[arr[x][y]] = 0
                if s:
                    dessert(x, y, c, f, s, k + 1)
            elif k == 2:
                if f:
                    kind[arr[x][y]] = 1
                    dessert(nx, ny, c + 1, f - 1, s, k)
                    kind[arr[x][y]] = 0
                else:
                    dessert(x, y, c, f, s, k + 1)
            else:
                kind[arr[x][y]] = 1
                dessert(nx, ny, c + 1, f, s, k)
                kind[arr[x][y]] = 0
        else:
            dessert(x, y, c, f, s, k + 1)


dx = [1, 1, -1, -1]
dy = [-1, 1, 1, -1]
for test_case in range(1, int(input()) + 1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr += [list(map(int, input().split()))]
    kind = [0] * 101
    max_count = 1
    for i in range(N - 2):
        for j in range(1, N - 1):
            ox = i
            oy = j
            kind[arr[i][j]] = 1
            dessert(i + 1, j - 1, 1, 1, 0, 0)
            kind[arr[i][j]] = 0
    if max_count == 1:
        max_count = -1
    print('#{} {}'.format(test_case, max_count))
