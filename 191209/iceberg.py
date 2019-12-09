import sys
sys.stdin = open('iceberg.txt', 'r')
from sys import *
setrecursionlimit(10 ** 6)


def check(x, y):
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < M and not arr[nx][ny]:
            ice[(x, y)] -= 1


def dfs(x, y):
    visit[x][y] = 1
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] and not visit[nx][ny]:
            dfs(nx, ny)


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
count = 0
time = 0
ice = {}
for i in range(N):
    for j in range(M):
        if arr[i][j]:
            ice[(i, j)] = arr[i][j]
while count < 2:
    for x, y in ice:
        check(x, y)
    for (x, y), value in ice.items():
        arr[x][y] = value
        if arr[x][y] < 0:
            arr[x][y] = 0
    for key, value in ice.items():
        if not value:
            ice.pop(key)
    count = 0
    time += 1
    visit = [[0] * M for _ in range(N)]
    for i, j in ice:
        if not visit[i][j]:
            dfs(i, j)
            count += 1
    if not count:
        time = 0
        break
print(time)
