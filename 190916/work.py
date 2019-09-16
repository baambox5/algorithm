import sys
sys.stdin = open('work.txt', 'r')


def perm(k, visit, multi):
    global max_value
    if k == N:
        if max_value < multi:
            max_value = multi
        return
    elif multi < max_value:
        return
    else:
        for i in range(N):
            if not visit & (1 << i) and arr[k][i]:
                perm(k + 1, visit | (1 << i), multi * (arr[k][i] / 100))


for test_case in range(1, int(input()) + 1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr += [list(map(int, input().split()))]
    max_value = 0
    perm(0, 0, 1)
    max_value *= 100
    print('#{}'.format(test_case), end=' ')
    print('%.6f' % max_value)
