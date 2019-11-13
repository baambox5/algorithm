import sys
sys.stdin = open('find_mine.txt', 'r')


def find(x, y):
    count = 0
    for k in range(8):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < N:
            if arr[nx][ny] == '*':
                count += 1
                break
    if not count:
        copy_arr[x][y] = 0
    else:
        copy_arr[x][y] = 1


def dfs(x, y):
    visit[x][y] = 1
    for k in range(8):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < N:
            if copy_arr[x][y] == 0:
                if copy_arr[nx][ny] != -1 and not visit[nx][ny]:
                    dfs(nx, ny)


dx = [-1, 0, 1, -1, 0, 1, -1, 1]
dy = [-1, -1, -1, 1, 1, 1, 0, 0]
for test_case in range(1, int(input()) + 1):
    N = int(input())
    arr = []
    copy_arr = [[-1] * N for _ in range(N)]
    for _ in range(N):
        arr.append(input())
    click_count = 0
    visit = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '.':
                find(i, j)
    for i in range(N):
        for j in range(N):
            if copy_arr[i][j] == 0 and not visit[i][j]:
                click_count += 1
                dfs(i, j)
    for i in range(N):
        for j in range(N):
            if copy_arr[i][j] == 1 and not visit[i][j]:
                click_count += 1
    print('#{} {}'.format(test_case, click_count))
