import sys
sys.stdin = open('cook.txt', 'r')


def perm(k, s, visit):
    if k == half_N:
        result.append(taste())
        return
    else:
        for i in range(s, N):
            if visit & (1 << i):
                continue
            order[k] = i
            perm(k + 1, i + 1, visit | (1 << i))


def taste():
    sum_taste = 0
    for ox in range(half_N - 1):
        x = order[ox]
        for oy in range(ox + 1, half_N):
            sum_taste += arr[x][order[oy]] + arr[order[oy]][x]
    return sum_taste


for test_case in range(1, int(input()) + 1):
    N = int(input())
    arr = []
    half_N = N // 2
    order = [0] * (N // 2)
    result = []
    for _ in range(N):
        arr += [list(map(int, input().split()))]
    perm(0, 0, 0)
    min_taste = 1000000
    for i in range(len(result) // 2):
        diff = abs(result[i] - result[-i-1])
        if diff < min_taste:
            min_taste = diff
    print('#{} {}'.format(test_case, min_taste))
