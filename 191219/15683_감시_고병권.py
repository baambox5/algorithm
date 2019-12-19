import sys
sys.stdin = open('big_brother.txt', 'r')


def you(x, y, d, count):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return count
    elif arr[x][y] == 6:
        return count
    elif not arr[x][y] and not visit[x][y]:
        visit[x][y] = 1
        count += 1
    if d == 0:
        return you(x, y - 1, 0, count)
    elif d == 1:
        return you(x - 1, y, 1, count)
    elif d == 2:
        return you(x, y + 1, 2, count)
    else:
        return you(x + 1, y, 3, count)


def is_watching():
    pass


def big_brother(k):
    if k == cctv_count:
        is_watching()
    else:
        for j in range(4):
            direction[k] = j
            big_brother(k + 1)


N, M = map(int, input().split())
cctv = {}
wall_count = 0
delta = ((-1, 0), (0, -1), (1, 0), (0, 1))
cctv5 = []
visit = [[0] * M for _ in range(N)]
arr = []
for i in range(N):
    arr += [list(map(int, input().split()))]
    for j in range(M):
        if 1 <= arr[i][j] <= 4:
            cctv[(i, j)] = arr[i][j]
        elif arr[i][j] == 6:
            wall_count += 1
        elif arr[i][j] == 5:
            cctv5 += [(i, j)]
cctv_count = len(cctv)
direction = [0] * cctv_count
check_count = 0
for x, y in cctv5:
    for i in range(4):
        check_count += you(x, y, i, 0)
big_brother(0)
print(N * M - check_count - cctv_count - wall_count - len(cctv5))