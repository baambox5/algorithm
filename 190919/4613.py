import sys
sys.stdin = open('4613.txt', 'r')

for test_case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = []
    for _ in range(N):
        arr += [input()]
    count_w = 0
    min_count = M * N
    for i in range(N - 2):
        for w in range(M):
            if arr[i][w] != 'W':
                count_w += 1
        count_b = 0
        for j in range(i + 1, N - 1):
            for b in range(M):
                if arr[j][b] != 'B':
                    count_b += 1
            count_r = 0
            for k in range(j + 1, N):
                for r in range(M):
                    if arr[k][r] != 'R':
                        count_r += 1
            if min_count > count_b+count_r+count_w:
                min_count = count_b + count_r + count_w
    print('#{} {}'.format(test_case, min_count))
