import sys
sys.stdin = open('2468.txt', 'r')
from sys import *
setrecursionlimit(10 ** 6)


def dfs(x, y):
    if x != N-1 and arr[x+1][y] > k and not visit[x+1][y]:
        visit[x+1][y] = 1
        dfs(x+1, y)
    if y != N-1 and arr[x][y+1] > k and not visit[x][y+1]:
        visit[x][y+1] = 1
        dfs(x, y+1)
    if x != 0 and arr[x-1][y] > k and not visit[x-1][y]:
        visit[x-1][y] = 1
        dfs(x-1, y)
    if y != 0 and arr[x][y-1] > k and not visit[x][y-1]:
        visit[x][y-1] = 1
        dfs(x, y-1)


N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
max_count = 1
for k in range(1, 100):
    count = 0
    visit = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] > k and not visit[i][j]:
                count += 1
                visit[i][j] = 1
                dfs(i, j)
    if not count:
        break
    if count > max_count:
        max_count = count
print(max_count)