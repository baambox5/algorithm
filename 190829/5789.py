import sys
sys.stdin = open('5789.txt', 'r')

for test_case in range(1, int(input()) + 1):
    N, Q = map(int, input().split())
    arr = [0] * (N + 1)
    for i in range(1, Q + 1):
        L, R = map(int, input().split())
        for j in range(L, R + 1):
            arr[j] = i
    print('#{}'.format(test_case), end=' ')
    for i in range(1, N + 1):
        print('{}'.format(arr[i]), end=' ')
    print()
