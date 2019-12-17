import sys
sys.stdin = open('roulette.txt', 'r')
from collections import deque

dx = [0, 1]
dy = [-1, 0]
N, M, T = map(int, input().split())
arr = []
for _ in range(N):
    arr += [list(map(int, input().split()))]
for _ in range(T):
    x, d, k = map(int, input().split())
    for i in range(N // x):
        p = x * (i + 1) - 1
        Q = deque()
        for num in arr[p]:
            Q.append(num)
        for _ in range(k):
            if d:
                Q.append(Q.popleft())
            else:
                Q.appendleft(Q.pop())
        m = 0
        while Q:
            arr[p][m] = Q.popleft()
            m += 1
    count = 0
    sum_value = 0
    check = 0
    axis = set()
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                for nk in range(2):
                    nx = i + dx[nk]
                    ny = j + dy[nk]
                    if nx < N and arr[nx][ny] == arr[i][j]:
                        axis.add((nx, ny))
                        axis.add((i, j))
                        check = 1
                if not check:
                    sum_value += arr[i][j]
                    count += 1
    if check:
        for i, j in axis:
            arr[i][j] = 0
    elif count:
        aver = sum_value / count
        for i in range(N):
            for j in range(M):
                if arr[i][j]:
                    if arr[i][j] < aver:
                        arr[i][j] += 1
                    elif arr[i][j] > aver:
                        arr[i][j] -= 1
sum_num = 0
for i in range(N):
    for j in range(M):
        if arr[i][j]:
            sum_num += arr[i][j]
print(sum_num)
