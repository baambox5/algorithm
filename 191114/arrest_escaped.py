import sys
sys.stdin = open('arrest_escaped.txt', 'r')
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
IN = [['1', '2', '5', '6'], ['1', '3', '4', '5'], ['1', '2', '4', '7'], ['1', '3', '6', '7']]
OUT = [['1', '2', '4', '7'], ['1', '3', '6', '7'], ['1', '2', '5', '6'], ['1', '3', '4', '5']]
for test_case in range(1, int(input()) + 1):
    N, M, R, C, L = map(int, input().split())
    arr = []
    visit = [[0] * M for _ in range(N)]
    for _ in range(N):
        arr += [input().split()]
    Q = deque()
    Q.append((R, C, L - 1))
    visit[R][C] = 1
    while Q:
        x, y, time = Q.popleft()
        if time:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny] and arr[nx][ny] != '0':
                    check = 0
                    for j in range(4):
                        if arr[x][y] == OUT[i][j]:
                            check += 1
                        if arr[nx][ny] == IN[i][j]:
                            check += 1
                    if check == 2:
                        visit[nx][ny] = 1
                        Q.append((nx, ny, time - 1))
    count = 0
    for i in range(N):
        for j in range(M):
            if visit[i][j]:
                count += 1
    print('#{} {}'.format(test_case, count))
