import sys
sys.stdin = open('5176.txt', 'r')


def change(n):
    global idx
    if n <= N:
        change(n * 2)
        arr[n] = idx
        idx += 1
        change(n * 2 + 1)


for test_case in range(1, int(input()) + 1):
    N = int(input())
    arr = [0] * (N + 1)
    idx = 1
    for i in range(1, N + 1):
        arr[i] = i
    change(1)
    print('#{} {} {}'.format(test_case, arr[1], arr[N // 2]))
