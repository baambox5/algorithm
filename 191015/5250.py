import sys
sys.stdin = open('5250.txt', 'r')


# dijkstra (time over)
# dx = [0, -1, 0, 1]
# dy = [-1, 0, 1, 0]
# for test_case in range(1, int(input()) + 1):
#     N = int(input())
#     arr = []
#     for _ in range(N):
#         arr.append(list(map(int, input().split())))
#     D = [[0xffff] * N for _ in range(N)]
#     D[0][0] = 0
#     cnt = N ** 2
#     visit = [[False] * N for _ in range(N)]
#     while cnt:
#         MIN = 0xffff
#         for i in range(N):
#             for j in range(N):
#                 if D[i][j] == 0xffff:
#                     break
#                 if not visit[i][j] and MIN > D[i][j]:
#                     x = i
#                     y = j
#                     MIN = D[i][j]
#         visit[x][y] = True
#         for k in range(4):
#             nx = x + dx[k]
#             ny = y + dy[k]
#             if 0 <= nx < N and 0 <= ny < N:
#                 if arr[nx][ny] - arr[x][y] > 0:
#                     w = 1 + arr[nx][ny] - arr[x][y]
#                 else:
#                     w = 1
#                 if D[nx][ny] > D[x][y] + w:
#                     D[nx][ny] = D[x][y] + w
#         cnt -= 1
#     print('#{} {}'.format(test_case, D[N-1][N-1]))


# dijkstra
from queue import PriorityQueue

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
for test_case in range(1, int(input()) + 1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    D = [[0xffff] * N for _ in range(N)]
    visit = [[False] * N for _ in range(N)]
    D[0][0] = 0
    Q = PriorityQueue()
    Q.put((0, (0, 0)))
    while not Q.empty():
        d, (x, y) = Q.get()
        if d > D[x][y]: continue
        visit[x][y] = True
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if visit[nx][ny]:
                    continue
                if arr[nx][ny] - arr[x][y] > 0:
                    w = 1 + arr[nx][ny] - arr[x][y]
                else:
                    w = 1
                if D[nx][ny] > D[x][y] + w:
                    D[nx][ny] = D[x][y] + w
                    Q.put((D[nx][ny], (nx, ny)))
    print('#{} {}'.format(test_case, D[N - 1][N - 1]))


# BFS
# from collections import deque
#
# dx = [0, -1, 0, 1]
# dy = [-1, 0, 1, 0]
# for test_case in range(1, int(input()) + 1):
#     N = int(input())
#     arr = []
#     for _ in range(N):
#         arr.append(list(map(int, input().split())))
#     D = [[0xffff] * N for _ in range(N)]
#     Q = deque()
#     D[0][0] = 0
#     Q.append((0, 0))
#     while Q:
#         x, y = Q.popleft()
#         for k in range(4):
#             nx = x + dx[k]
#             ny = y + dy[k]
#             if 0 <= nx < N and 0 <= ny < N:
#                 if arr[nx][ny] - arr[x][y] > 0:
#                     w = 1 + arr[nx][ny] - arr[x][y]
#                 else:
#                     w = 1
#                 if D[nx][ny] > D[x][y] + w:
#                     D[nx][ny] = D[x][y] + w
#                     Q.append((nx, ny))
#     print('#{} {}'.format(test_case, D[N - 1][N - 1]))
