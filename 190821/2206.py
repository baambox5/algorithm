import sys
sys.stdin = open('2206.txt', 'r')
from collections import deque

for _ in range(8):
    N, M = map(int, input().split())
    visit = [[0] * M for _ in range(N)]
    D = [[0] * M for _ in range(N)]
    chance_arr = [[0] * M for _ in range(N)]
    arr = []
    for _ in range(N):
        arr.append(input())
    Q = deque()
    Q.append((0, 0, 1))
    D[0][0] = 1
    visit[0][0] = 1
    chance_arr[0][0] = 1
    while Q:
        x, y, chance = Q.popleft()
        if y != M-1:
            if not visit[x][y + 1] and (arr[x][y + 1] == '0' or chance):
                if arr[x][y + 1] == '1':
                    Q.append((x, y + 1, 0))
                else:
                    Q.append((x, y + 1, chance))
                chance_arr[x][y + 1] = chance
                visit[x][y + 1] = 1
                D[x][y + 1] = D[x][y] + 1
            if visit[x][y + 1] and arr[x][y + 1] == '0' and chance and not chance_arr[x][y + 1]:
                Q.append((x, y + 1, 1))
                chance_arr[x][y + 1] = 1
                D[x][y + 1] = D[x][y] + 1
        if x != N-1:
            if not visit[x + 1][y] and (arr[x + 1][y] == '0' or chance):
                if arr[x + 1][y] == '1':
                    Q.append((x + 1, y, 0))
                else:
                    Q.append((x + 1, y, chance))
                chance_arr[x + 1][y] = chance
                visit[x + 1][y] = 1            
                D[x + 1][y] = D[x][y] + 1
            if visit[x + 1][y] and arr[x + 1][y] == '0' and chance and not chance_arr[x + 1][y]:
                Q.append((x + 1, y, 1))
                chance_arr[x + 1][y] = 1
                D[x + 1][y] = D[x][y] + 1
        if y != 0:
            if not visit[x][y - 1] and (arr[x][y - 1] == '0' or chance):
                if arr[x][y - 1] == '1':
                    Q.append((x, y - 1, 0))
                else:
                    Q.append((x, y - 1, chance))
                chance_arr[x][y - 1] = chance
                visit[x][y - 1] = 1
                D[x][y - 1] = D[x][y] + 1
            if visit[x][y - 1] and arr[x][y - 1] == '0' and chance and not chance_arr[x][y - 1]:
                Q.append((x, y - 1, 1))
                chance_arr[x][y - 1] = 1
                D[x][y - 1] = D[x][y] + 1
        if x != 0:
            if not visit[x - 1][y] and (arr[x - 1][y] == '0' or chance):
                if arr[x - 1][y] == '1':
                    Q.append((x - 1, y, 0))
                else:
                    Q.append((x - 1, y, chance))
                chance_arr[x - 1][y] = chance
                visit[x - 1][y] = 1            
                D[x - 1][y] = D[x][y] + 1
            if visit[x - 1][y] and arr[x - 1][y] == '0' and chance and not chance_arr[x - 1][y]:
                Q.append((x - 1, y, 1))
                chance_arr[x - 1][y] = 1
                D[x - 1][y] = D[x][y] + 1
        if x == N - 1 and y == M - 1:
            break
    if D[N - 1][M - 1]:
        print(D[N - 1][M - 1])
    else:
        print('-1')
