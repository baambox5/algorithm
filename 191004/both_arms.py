import sys
sys.stdin = open('both_arms.txt', 'r')


def perm(k, visit, n):
    if k == n:

        return
    else:
        for i in range(N):
            if visit & (1 << i):
                continue
            order[k] = 1
            perm(k + 1, visit | (1 << i), n)


for test_case in range(1, int(input()) + 1):
    N = int(input())
    weight = list(map(int, input().split()))
    fn = [1] * (N + 1)
    for i in range(1, N + 1):
        fn[i] = i * fn[i - 1]
    count = 0
    count += fn[N]
    order = [0] * N
    for i in range(1, N):
        perm(0, 0, i)
    print('#{} {}'.format(test_case, count))
