import sys
sys.stdin = open('5105.txt', 'r')
from collections import deque

for test_case in range(1, int(input()) + 1):
    q = deque()
    N = int(input())
    arr = []
    visit = [[0] * N for _ in range(N)]
    dist = [[0] * N for _ in range(N)]
    flag = 1
    for _ in range(N):
        arr.append(input())
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                visit[i][j] = 1
                q.append((i, j))
                while q:
                    x, y = q.popleft()
                    if arr[x][y] == '3':
                        print('#{} {}'.format(test_case, dist[x][y]-1))
                        flag = 0
                        break
                    if y != N-1 and arr[x][y+1] != '1' and not visit[x][y+1]:
                        visit[x][y + 1] = 1
                        dist[x][y + 1] = dist[x][y] + 1
                        q.append((x, y + 1))
                    if x != N-1 and arr[x+1][y] != '1' and not visit[x+1][y]:
                        visit[x + 1][y] = 1
                        dist[x + 1][y] = dist[x][y] + 1
                        q.append((x + 1, y))
                    if y != 0 and arr[x][y-1] != '1' and not visit[x][y-1]:
                        visit[x][y - 1] = 1
                        dist[x][y - 1] = dist[x][y] + 1
                        q.append((x, y - 1))
                    if x != 0 and arr[x-1][y] != '1' and not visit[x-1][y]:
                        visit[x - 1][y] = 1
                        dist[x - 1][y] = dist[x][y] + 1
                        q.append((x - 1, y))
                if flag:
                    print('#{} {}'.format(test_case, 0))
                break
