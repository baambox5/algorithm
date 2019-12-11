import sys
sys.stdin = open('research.txt', 'r')
from collections import deque
import copy


def perm(k, s):
    global sum_count, max_count
    if k == 3:
        new_arr = copy.deepcopy(arr)
        sum_count = 0
        for j in order:
            x, y = zero[j]
            new_arr[x][y] = '1'
        for x, y in virus:
            bfs(x, y, new_arr)
            if zero_count - 3 - sum_count <= max_count:
                break
        if zero_count - 3 - sum_count > max_count:
            max_count = zero_count - 3 - sum_count
    else:
        for i in range(s, zero_count):
            order[k] = i
            perm(k + 1, i + 1)


def bfs(x, y, n_arr):
    global sum_count
    Q = deque()
    Q.append((x, y))
    while Q:
        x, y = Q.popleft()
        for dx, dy in delta:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M and n_arr[nx][ny] == '0':
                n_arr[nx][ny] = '2'
                Q.append((nx, ny))
                sum_count += 1


delta = ((-1, 0), (0, -1), (1, 0), (0, 1))
N, M = map(int, input().split())
arr = []
zero = []
zero_count = 0
virus = []
max_count = 0
sum_count = 0
order = [0] * 3
for i in range(N):
    arr += [input().split()]
    for j in range(M):
        if arr[i][j] == '0':
            zero.append((i, j))
            zero_count += 1
        elif arr[i][j] == '2':
            virus.append((i, j))
perm(0, 0)
print(max_count)
