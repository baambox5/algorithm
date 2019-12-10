import sys
sys.stdin = open('treasure.txt', 'r')
from collections import deque

N, M = map(int, input().split())
arr = [input() for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
Q = deque()
longest = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            visit = [[0] * M for _ in range(N)]
            Q.append((i, j, 0))
            visit[i][j] = 1
            while Q:
                x, y, d = Q.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 'L' and not visit[nx][ny]:
                        Q.append((nx, ny, d + 1))
                        visit[nx][ny] = 1
            if longest < d:
                longest = d
print(longest)
