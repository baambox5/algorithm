import sys
sys.stdin = open('4875.txt', 'r')
from collections import deque

for test_case in range(1, int(input()) + 1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(input())
    Q = deque()
    visit = [[0] * N for _ in range(N)]
    res = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                Q.append((i, j))
                visit[i][j] = 1
                while Q:
                    x, y = Q.popleft()
                    if arr[x][y] == '3':
                        res = 1
                        break
                    if y != N-1 and (arr[x][y+1] == '0' or arr[x][y+1] == '3') and not visit[x][y+1]:
                        visit[x][y + 1] = 1
                        Q.append((x, y + 1))
                    if x != N-1 and (arr[x+1][y] == '0' or arr[x+1][y] == '3') and not visit[x+1][y]:
                        visit[x + 1][y] = 1
                        Q.append((x + 1, y))
                    if y != 0 and (arr[x][y-1] == '0' or arr[x][y-1] == '3') and not visit[x][y-1]:
                        visit[x][y-1] = 1
                        Q.append((x, y-1))
                    if x != 0 and (arr[x-1][y] == '0' or arr[x-1][y] == '3') and not visit[x-1][y]:
                        visit[x - 1][y] = 1
                        Q.append((x - 1, y))
                break
    print('#{} {}'.format(test_case, res))

