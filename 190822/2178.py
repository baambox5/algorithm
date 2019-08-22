import sys
sys.stdin = open('2178.txt', 'r')
from collections import deque

for _ in range(4):
    N, M = map(int, input().split())
    arr = []
    visit = [[0] * M for _ in range(N)]
    for _ in range(N):
        arr += [input()]
    D = [[0] * M for _ in range(N)]
    Q = deque()
    Q.append((0, 0))
    visit[0][0] = 1
    x, y = 0, 0
    D[0][0] = 1
    while Q:
        x, y = Q.popleft()
        if y != M-1 and arr[x][y + 1] == '1' and not visit[x][y + 1]:
            visit[x][y + 1] = 1
            Q.append((x, y + 1))
            D[x][y + 1] = D[x][y] + 1
        if x != N-1 and arr[x + 1][y] == '1' and not visit[x + 1][y]:
            visit[x + 1][y] = 1
            Q.append((x + 1, y))
            D[x + 1][y] = D[x][y] + 1
        if x != 0 and arr[x - 1][y] == '1' and not visit[x - 1][y]:
            visit[x - 1][y] = 1
            Q.append((x - 1, y))
            D[x - 1][y] = D[x][y] + 1
        if y != 0 and arr[x][y - 1] == '1' and not visit[x][y - 1]:
            visit[x][y - 1] = 1
            Q.append((x, y - 1))
            D[x][y - 1] = D[x][y] + 1
        if x == N - 1 and y == M - 1:
            break
    print(D[N-1][M-1])