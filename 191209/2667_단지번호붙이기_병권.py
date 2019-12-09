import sys
sys.stdin = open('attach_number.txt', 'r')

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
N = int(input())
arr = []
for _ in range(N):
    arr += [input()]
visit = [[0] * N for _ in range(N)]
count = 0
house = []


def dfs(x, y):
    visit[x][y] = 1
    house[count] += 1
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == '1' and not visit[nx][ny]:
            dfs(nx, ny)


for i in range(N):
    for j in range(N):
        if arr[i][j] == '1' and not visit[i][j]:
            house.append(0)
            dfs(i, j)
            count += 1
house.sort()
print(count)
for num in house:
    print(num)
