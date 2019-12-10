import sys
sys.stdin = open('iceberg.txt', 'r')
from collections import deque


def check(x, y):
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < M and not arr[nx][ny]:
            ice[(x, y)] -= 1


def bfs(x, y):
    Q = deque()
    visit[x][y] = 1
    Q.append((x, y))
    while Q:
        i, j = Q.popleft()
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] and not visit[nx][ny]:
                Q.append((nx, ny))
                visit[nx][ny] = 1


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
count = 0
time = 0
ice = {}
visit = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j]:
            ice[(i, j)] = arr[i][j]
while count < 2:
    new_ice = {}
    for i, j in ice:
        check(i, j)
    for (i, j), value in ice.items():
        if value < 0:
            value = 0
        arr[i][j] = value
        if value:
            new_ice[(i, j)] = value
    count = 0
    time += 1
    for i, j in new_ice:
        if not visit[i][j]:
            bfs(i, j)
            count += 1
            if count >= 2:
                break
    if count >= 2:
        break
    elif not count:
        time = 0
        break
    for i, j in new_ice:
        visit[i][j] = 0
    ice = new_ice
print(time)
