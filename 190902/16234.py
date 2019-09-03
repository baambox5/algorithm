import sys
sys.stdin = open('16234.txt', 'r')
from sys import *
setrecursionlimit(10 ** 6)

def dfs(x, y):
    global count, sum_value
    count += 1
    sum_value += arr[x][y]
    calc.append((x, y))
    for i in range(4):
        r_d = x + row_d[i]
        c_d = y + column_d[i]
        if 0 <= r_d < N and 0 <= c_d < N and not visit[r_d][c_d]:
            diff = arr[x][y] - arr[r_d][c_d]
            if diff < 0:
                diff = -diff
            if R >= diff >= L:
                visit[r_d][c_d] = 1
                dfs(r_d, c_d)


N, L, R = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
res_count = 0
row_d = [-1, 0, 1, 0]
column_d = [0, -1, 0, 1]
while res_count < 2000:
    visit = [[0] * N for _ in range(N)]
    flag = 0
    for i in range(N):
        for j in range(N):
            if not visit[i][j]:
                visit[i][j] = 1
                calc = []
                count = 0
                sum_value = 0
                dfs(i, j)
                if count > 1:
                    flag = 1
                    for a, b in calc:
                        arr[a][b] = sum_value // count
    if not flag:
        break
    res_count += 1
print(res_count)
