import sys
sys.stdin = open('4881.txt', 'r')


def perm(k, n, visit, low_sum):
    if k == n:
        return my_sum(n)
    else:
        for i in range(n):
            if visit & (1 << i): continue
            order[k] = i
            sum_value = perm(k + 1, n, visit | (1 << i), low_sum)
            if sum_value < low_sum:
                low_sum = sum_value
        else:
            return low_sum


def my_sum(n):
    sum_value = 0
    for i in range(n):
        sum_value += arr[i][order[i]]
    return sum_value


for test_case in range(1, int(input()) + 1):
    N = int(input())
    arr = []
    order = [0] * N
    for _ in range(N):
        arr += [list(map(int, input().split()))]
    print('#{} {}'.format(test_case, perm(0, N, 0, 100)))
