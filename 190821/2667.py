import sys
sys.stdin = open('2667.txt', 'r')


def dfs(x, y):
    visit[x][y] = 1
    inner_count = 1
    if y != N-1 and arr[x][y + 1] == '1' and not visit[x][y + 1]:
        inner_count += dfs(x, y + 1)
    if x != N-1 and arr[x + 1][y] == '1' and not visit[x + 1][y]:
        inner_count += dfs(x + 1, y)
    if y != 0 and arr[x][y - 1] == '1' and not visit[x][y-1]:
        inner_count += dfs(x, y - 1)
    if x != 0 and arr[x - 1][y] == '1' and not visit[x - 1][y]:
        inner_count += dfs(x - 1, y)
    return inner_count


N = int(input())
arr = []
for _ in range(N):
    arr += input().split()
visit = [[0] * N for _ in range(N)]
count = 0
res = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == '1' and not visit[i][j]:
            count += 1
            res.append(dfs(i, j))
print(count)
min_value = N
for i in range(len(res)):
    for j in range(i, len(res)):
        if res[i] > res[j]:
            res[i], res[j] = res[j], res[i]
    print(res[i])
