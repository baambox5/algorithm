import sys
sys.stdin = open('2206.txt', 'r')
from collections import deque

for _ in range(2):
    N, M = map(int, input().split())
    visit = [[0] * M for _ in range(N)]
    D = [[0] * M for _ in range(N)]
    arr = []
    for _ in range(N):
        arr.append(input())
    Q = deque()
    Q.append((0, 0, 1))
    D[0][0] = 1
    visit[0][0] = 1
    chance_x = 0
    chance_y = 0
    while Q:
        x, y, chance = Q.popleft()
        if chance_x == x and chance_y == y and not chance:
            chance = 1
            D[x][y] -= 2
        if y != M-1 and (arr[x][y + 1] == '0' or chance) and not visit[x][y + 1]:
            if arr[x][y + 1] == '1':
                chance = 0
                chance_x, chance_y = x, y
                visit[x][y] = 0
            visit[x][y + 1] = 1
            Q.append((x, y + 1, chance))
            D[x][y + 1] = D[x][y] + 1
        if x != N-1 and (arr[x + 1][y] == '0' or chance) and not visit[x + 1][y]:
            if arr[x + 1][y] == '1':
                chance = 0
                chance_x, chance_y = x, y
                visit[x][y] = 0
            visit[x + 1][y] = 1
            Q.append((x + 1, y, chance))
            D[x + 1][y] = D[x][y] + 1
        if y != 0 and (arr[x][y - 1] == '0' or chance) and not visit[x][y - 1]:
            if arr[x][y - 1] == '1':
                chance = 0
                chance_x, chance_y = x, y
                visit[x][y] = 0
            visit[x][y - 1] = 1
            Q.append((x, y - 1, chance))
            D[x][y - 1] = D[x][y] + 1
        if x != 0 and (arr[x - 1][y] == '0' or chance) and not visit[x - 1][y]:
            if arr[x - 1][y] == '1':
                chance = 0
                chance_x, chance_y = x, y
                visit[x][y] = 0
            visit[x - 1][y] = 1
            Q.append((x - 1, y, chance))
            D[x - 1][y] = D[x][y] + 1
        if x == N - 1 and y == M - 1:
            break
    if D[N - 1][M - 1]:
        print(D[N - 1][M - 1])
    else:
        print('-1')
