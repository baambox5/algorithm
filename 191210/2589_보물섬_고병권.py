import sys
sys.stdin = open('treasure.txt', 'r')
from collections import deque

N, M = map(int, input().split())
arr = []
L_axis = set()
for i in range(N):
    arr += [input()]
    for j in range(M):
        if arr[i][j] == 'L':
            L_axis.add((i, j))
delta = ((-1, 0), (0, -1), (1, 0), (0, 1))
Q = deque()
longest = 0
visit = [[0] * M for _ in range(N)]
for i, j in L_axis:
    Q.append((i, j, 0))
    visit[i][j] = 1
    while Q:
        x, y, d = Q.popleft()
        for dx, dy in delta:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 'L' and not visit[nx][ny]:
                Q.append((nx, ny, d + 1))
                visit[nx][ny] = 1
    if longest < d:
        longest = d
    for k, l in L_axis:
        visit[k][l] = 0
print(longest)
