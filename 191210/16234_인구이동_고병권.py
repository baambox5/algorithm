import sys
sys.stdin = open('people.txt', 'r')
import sys
sys.setrecursionlimit(10 ** 6)

def dfs(x, y):
    global sum_people, count
    visit[x][y] = 1
    count += 1
    sum_people += arr[x][y]
    new_union.add((x, y))
    for dx, dy in delta:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N and 0 <= ny < N and not visit[nx][ny]:
            diff = arr[nx][ny] - arr[x][y]
            if diff < 0:
                diff = - diff
            if L <= diff <= R:
                dfs(nx, ny)


delta = ((-1, 0), (0, -1), (1, 0), (0, 1))
N, L, R = map(int, input().split())
people = 0
arr = [list(map(int, input().split())) for _ in range(N)]
move = 0
while move <= 2000:
    union = 0
    visit = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visit[i][j]:
                sum_people = 0
                count = 0
                new_union = set()
                dfs(i, j)
                if count >= 2:
                    union = 1
                    for x, y in new_union:
                        arr[x][y] = sum_people // count
    if not union:
        break
    move += 1
print(move)
