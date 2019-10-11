import sys
sys.stdin = open('5177.txt', 'r')


def check(n):
    global idx
    if n:
        if arr[idx] < arr[n]:
            arr[n], arr[idx] = arr[idx], arr[n]
            idx = n
            check(n // 2)


def sum_tree(n):
    global sum_value
    if n:
        sum_value += arr[n]
        sum_tree(n // 2)


for test_case in range(1, int(input()) + 1):
    N = int(input())
    arr = [0] * (N + 1)
    num_in = list(map(int, input().split()))
    for i in range(1, N + 1):
        arr[i] = num_in[i - 1]
        idx = i
        check(i // 2)
    sum_value = 0
    sum_tree(N // 2)
    print('#{} {}'.format(test_case, sum_value))
