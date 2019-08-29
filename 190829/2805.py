import sys
sys.stdin = open('2805.txt', 'r')

for test_case in range(1, int(input()) + 1):
    N = int(input())
    arr = [[] * N for _ in range(N)]
    for i in range(N):
        for j in input():
            arr[i] += [int(j)]
    res = 0
    for i in range(N // 2):
        for j in range(i + 1):
            if j:
                res += arr[i][N // 2 - j] + arr[i][N // 2 + j]
            else:
                res += arr[i][N // 2]
    for i in range(N // 2, -1, -1):
        for j in range(i + 1):
            if j:
                res += arr[N-i-1][N // 2 - j] + arr[N-i-1][N // 2 + j]
            else:
                res += arr[N-i-1][N // 2]
    print('#{} {}'.format(test_case, res))
