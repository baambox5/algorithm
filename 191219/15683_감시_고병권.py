import sys
sys.stdin = open('big_brother.txt', 'r')


def you(x, y, d, count):
    if x == -1 or x == N or y == -1 or y == M:
        return count
    elif arr[x][y] == 6:
        return count
    elif not arr[x][y] and not copied_visit[x][y]:
        copied_visit[x][y] = 1
        count += 1
    if d == 0:
        return you(x, y - 1, 0, count)
    elif d == 1:
        return you(x - 1, y, 1, count)
    elif d == 2:
        return you(x, y + 1, 2, count)
    elif d == 3:
        return you(x + 1, y, 3, count)


def is_watching():
    global max_count
    cnt = 0
    for i in range(cctv_count):
        x, y, type = cctv[i]
        if type == 1:
            cnt += you(x, y, direction[i], 0)
        elif type == 2:
            if direction[i] == 2 or direction[i] == 3:
                continue
            cnt += you(x, y, direction[i], 0)
            cnt += you(x, y, direction[i] + 2, 0)
        elif type == 3:
            cnt += you(x, y, direction[i], 0)
            if direction[i] == 3:
                cnt += you(x, y, 0, 0)
            else:
                cnt += you(x, y, direction[i] + 1, 0)
        elif type == 4:
            if not direction[i]:
                cnt += you(x, y, 3, 0)
            else:
                cnt += you(x, y, direction[i] - 1, 0)
            cnt += you(x, y, direction[i], 0)
            if direction[i] == 3:
                cnt += you(x, y, 0, 0)
            else:
                cnt += you(x, y, direction[i] + 1, 0)
    if cnt > max_count:
        max_count = cnt


def big_brother(k):
    global copied_visit
    if k == cctv_count:
        copied_visit = [[0] * M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                if visit[i][j]:
                    copied_visit[i][j] = 1
        is_watching()
    else:
        for j in range(4):
            direction[k] = j
            big_brother(k + 1)


N, M = map(int, input().split())
cctv = []
wall_count = 0
cctv5 = []
copied_visit = [[0] * M for _ in range(N)]
visit = [[0] * M for _ in range(N)]
arr = []
for i in range(N):
    arr += [list(map(int, input().split()))]
    for j in range(M):
        if 1 <= arr[i][j] <= 4:
            cctv += [(i, j, arr[i][j])]
        elif arr[i][j] == 6:
            wall_count += 1
        elif arr[i][j] == 5:
            cctv5 += [(i, j)]
cctv_count = len(cctv)
direction = [0] * cctv_count
check_count = 0
max_count = 0
for x, y in cctv5:
    for i in range(4):
        check_count += you(x, y, i, 0)
for i in range(N):
    for j in range(M):
        if copied_visit[i][j]:
            visit[i][j] = 1
if cctv_count:
    big_brother(0)
print(N * M - check_count - cctv_count - wall_count - len(cctv5) - max_count)
