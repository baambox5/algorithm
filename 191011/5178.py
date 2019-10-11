import sys
sys.stdin = open('5178.txt', 'r')


def sum_tree(n):
    if n:
        arr[n] += v
        sum_tree(n // 2)


for test_case in range(1, int(input()) + 1):
    N, M, L = map(int, input().split())
    arr = [0] * (N + 1)
    for _ in range(M):
        i, v = map(int, input().split())
        arr[i] = v
        sum_tree(i // 2)
    print('#{} {}'.format(test_case, arr[L]))
