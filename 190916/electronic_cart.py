import sys
sys.stdin = open('electronic_cart.txt', 'r')


def perm(k, visit, s):
    global min_value
    if k == N-1:
        s += arr[order[k-1]][0]
        if min_value > s:
            min_value = s
        return
    elif min_value < s:
        return
    else:
        for i in range(1, N):
            if not visit & (1 << i) and order[k-1] != i:
                order[k] = i
                perm(k + 1, visit | (1 << i), s + arr[order[k-1]][i])


for test_case in range(1, int(input()) + 1):
    N = int(input())
    order = [0] * N
    arr = []
    min_value = 1000000
    for _ in range(N):
        arr += [list(map(int, input().split()))]
    perm(0, 0, 0)
    print('#{} {}'.format(test_case, min_value))
