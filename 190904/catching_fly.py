import sys
sys.stdin = open('catching_fly.txt', 'r')

for test_case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    max_sum = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            sum_value = 0
            for k in range(i, i + M):
                for l in range(j, j + M):
                    sum_value += arr[k][l]
            if sum_value > max_sum:
                max_sum = sum_value
    print('#{} {}'.format(test_case, max_sum))
