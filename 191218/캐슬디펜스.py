import itertools

N, M, D = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
enemy = []
for i in range(N):
    for j in range(M):
        if arr[i][j]:
            enemy.append([i, j])

cols = itertools.combinations([i for i in range(M)], 3)
MAP = [[0] * M for _ in range(N)]
ans = 0
for col in cols:
    for i in range(N):
        for j in range(M):
            MAP[i][j] = arr[i][j]
    cnt = 0
    tx, ty = [0] * 3, [0] * 3
    for end in range(N - 1, -1, -1):
        row = end + 1
        d = [0xfff] * 3
        for i in range(3):
            for x, y in enemy:
                if x > end or MAP[x][y] == 0: continue
                dist = abs(row - x) + abs(y - col[i])
                if dist <= D and dist < d[i]:
                    d[i], tx[i], ty[i] = dist, x, y
                elif d[i] == dist and y < ty[i]:
                    tx[i], ty[i] = x, y

        for i in range(3):
            if d[i] != 0xfff and MAP[tx[i]][ty[i]]:
                cnt += 1
                MAP[tx[i]][ty[i]] = 0
    ans = max(ans, cnt)


print(ans)




