import sys
sys.stdin = open('break_brick.txt', 'r')
import copy
from collections import deque


def perm(k, c_arr, cnt, c_big):
    global min_count
    if k == N:
        if cnt < 0:
            cnt = 0
        if cnt < min_count:
            min_count = cnt
        return
    for i, j, w in c_big:
        Q = deque()
        copy_arr = copy.deepcopy(c_arr)
        for d in range(1, w):
            copy_arr[i-d][j] = 0
        Q.append((i, j, copy_arr[i][j]))
        copy_arr[i][j] = 0
        while Q:
            x, y, z = Q.popleft()
            for d in range(-z + 1, z):
                dx = x + d
                dy = y + d
                if 0 <= dx < H:
                    if copy_arr[dx][y] > 1:
                        Q.append((dx, y, copy_arr[dx][y]))
                    copy_arr[dx][y] = 0
                if 0 <= dy < W:
                    if copy_arr[x][dy] > 1:
                        Q.append((x, dy, copy_arr[x][dy]))
                    copy_arr[x][dy] = 0
        count = [0] * W
        copy_big = []
        big = []
        cnt = 0
        for j in range(W):
            for i in range(H):
                if copy_arr[i][j]:
                    count[j] += 1
                    cnt += 1
                    if copy_arr[i][j] > 1:
                        big.append((j, count[j], copy_arr[i][j]))

        copy_arr = [[0] * W for _ in range(H)]
        for j in range(W):
            for i in range(count[j]):
                copy_arr[H-i-1][j] = 1
        for j, c, v in big:
            i = H-1-(count[j]-c)
            copy_arr[i][j] = v
            if N - k - w >= c and count[j]:
                copy_big.append((i, j, c))
        if copy_big:
            perm(k + w, copy_arr, cnt, copy_big)
        else:
            perm(N, [], cnt - N + k + w, [])


for test_case in range(1, int(input()) + 1):
    N, W, H = map(int, input().split())
    arr = [0 for _ in range(H)]
    count = [0] * W
    total_count = 0
    big_one = []
    for i in range(H):
        arr[i] = list(map(int, input().split()))
        for j in range(W):
            if arr[i][j]:
                count[j] += 1
                total_count += 1
                if arr[i][j] > 1 and N >= count[j]:
                    big_one.append((i, j, count[j]))
    min_count = total_count
    if big_one:
        perm(0, arr, total_count, big_one)
    else:
        min_count -= N
    print('#{} {}'.format(test_case, min_count))
