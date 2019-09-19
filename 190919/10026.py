import sys
sys.stdin = open('10026.txt', 'r')
sys.setrecursionlimit(10**6)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
def dfs(x, y, s, flag):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if flag:
                if arr[nx][ny] == s and not visit_normal[nx][ny]:
                    visit_normal[nx][ny] = 1
                    dfs(nx, ny, s, flag)
            else:
                if not visit_sick[nx][ny] and (arr[nx][ny] == s or (s == 'R' and arr[nx][ny] == 'G') or (s == 'G' and arr[nx][ny] == 'R')):
                    visit_sick[nx][ny] = 1
                    dfs(nx, ny, s, flag)


N = int(input())
arr = []
for _ in range(N):
    arr += [input()]
count_sick = 0
count_normal = 0
visit_sick = [[0] * N for _ in range(N)]
visit_normal = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visit_normal[i][j]:
            count_normal += 1
            visit_normal[i][j] = 1
            dfs(i, j, arr[i][j], 1)
        if not visit_sick[i][j]:
            count_sick += 1
            visit_sick[i][j] = 1
            dfs(i, j, arr[i][j], 0)
print(count_normal, count_sick)
