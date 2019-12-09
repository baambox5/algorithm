import sys
sys.stdin = open('safety_area.txt', 'r')
from sys import *
setrecursionlimit(10 ** 6)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
max_area = 1
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def dfs(x, y):
    visit[x][y] = 1
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] > h and not visit[nx][ny]:
            dfs(nx, ny)


for h in range(1, 100):
    visit = [[0] * N for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > h and not visit[i][j]:
                dfs(i, j)
                count += 1
    if not count:
        break
    if max_area < count:
        max_area = count
print(max_area)
