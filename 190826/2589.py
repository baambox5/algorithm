import sys
sys.stdin = open('2589.txt', 'r')
from collections import deque

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(input())
max_count = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            visit = [[0] * M for _ in range(N)]
            Q = deque()
            Q.append((i, j, 0))
            visit[i][j] = 1
            while Q:
                x, y, count = Q.popleft()
                if max_count < count:
                    max_count = count
                if x != N-1 and arr[x+1][y] == 'L' and not visit[x+1][y]:
                    visit[x+1][y] = 1
                    Q.append((x+1, y, count+1))
                if y != M-1 and arr[x][y+1] == 'L' and not visit[x][y+1]:
                    visit[x][y+1] = 1
                    Q.append((x, y+1, count+1))
                if x != 0 and arr[x-1][y] == 'L' and not visit[x-1][y]:
                    visit[x-1][y] = 1
                    Q.append((x-1, y, count+1))
                if y != 0 and arr[x][y-1] == 'L' and not visit[x][y-1]:
                    visit[x][y-1] = 1
                    Q.append((x, y-1, count+1))
print(max_count)