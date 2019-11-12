import sys
sys.stdin = open('hiking_trail.txt', 'r')


def dfs(x, y, count, check):
    global max_count
    visit[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if visit[nx][ny]:
                continue
            if arr[x][y] > arr[nx][ny]:
                dfs(nx, ny, count + 1, check)
            if check:
                diff = arr[nx][ny] - arr[x][y] + 1
                if K >= diff > 0:
                    arr[nx][ny] -= diff
                    dfs(nx, ny, count + 1, 0)
                    arr[nx][ny] += diff
    if count > max_count:
        max_count = count
    visit[x][y] = 0


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
for test_case in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    high_number = 0
    max_count = 0
    visit = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] > high_number:
                high_number = arr[i][j]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == high_number:
                dfs(i, j, 1, 1)
    print('#{} {}'.format(test_case, max_count))
