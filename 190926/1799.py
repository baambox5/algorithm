import sys
sys.stdin = open('1799.txt', 'r')


def check_func(q, w):
    for s in range(1, N):
        if s <= q and s <= w:
            check[q - s][w - s] = 1
        if s <= q and w < N - s:
            check[q - s][w + s] = 1
        if q < N - s and s <= w:
            check[q + s][w - s] = 1
        if q < N - s and w < N - s:
            check[q + s][w + s] = 1


def dfs(x, y, count):
    global count_1, count_2
    visit[x][y] = 1
    for p in range(1, N):
        dx = [-p, -p, p, p]
        dy = [-p, p, p, -p]
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if visit[nx][ny]:
                   continue
                if not check[nx][ny] and arr[nx][ny] == '1':
                    check_func(nx, ny)
                    dfs(nx, ny, count + 1)
                else:
                    dfs(nx, ny, count)
    if d:
        if count_1 < count:
            count_1 = count
    else:
        if count_2 < count:
            count_2 = count


N = int(input())
arr = []
for i in range(N):
    arr.append(input().split())
count_1 = 0
count_2 = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == '1':
            visit = [[0] * N for _ in range(N)]
            check = [[0] * N for _ in range(N)]
            check_func(i, j)
            if not i % 2:
                if j % 2:
                    d = 1
                    dfs(i, j, 1)
                else:
                    d = 0
                    dfs(i, j, 1)
            else:
                if not j % 2:
                    d = 1
                    dfs(i, j, 1)
                else:
                    d = 0
                    dfs(i, j, 1)
print(count_1 + count_2)
