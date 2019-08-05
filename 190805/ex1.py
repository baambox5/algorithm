arr = [[9, 20, 2, 18, 11],
       [19, 1, 25, 3, 21],
       [8, 24, 10, 17, 7],
       [15, 4, 16, 5, 6],
       [12, 13, 22, 23, 14]]

N, M = len(arr), len(arr[0])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

num_sum = 0
val = 0
for x in range(N):
    for y in range(M):
        for i in range(4):
            tx, ty = x + dx[i], y + dy[i]
            if tx < 0 or ty < 0 or tx == N or ty == M:
                continue
            val = arr[tx][ty]-arr[x][y]
            num_sum += -val if val < 0 else val

print('{}'.format(num_sum))
