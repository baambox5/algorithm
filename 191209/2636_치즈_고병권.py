import sys
sys.stdin = open('cheese.txt', 'r')


def outskirt_dfs(x, y):
    arr[x][y] = -1
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == '0':
            outskirt_dfs(nx, ny)


def check(x, y):
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == -1:
            arr[x][y] = 0


N, M = map(int, input().split())
arr = []
cheese = 0
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
for i in range(N):
    arr += [input().split()]
    for j in range(M):
        if arr[i][j] == '1':
            cheese += 1
time = 0
outskirt_dfs(0, 0)
remain = 0
while cheese:
    remain = cheese
    for i in range(N):
        for j in range(M):
            if arr[i][j] == '1':
                check(i, j)
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                outskirt_dfs(i, j)
                cheese -= 1
    time += 1
print(time)
print(remain)
