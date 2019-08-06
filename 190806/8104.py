import sys
sys.stdin = open('8104.txt', 'r')

for test_case in range(1, int(input()) + 1):
    N, K = tuple(map(int, input().split()))
    arr = []
    for i in range(K):
        arr.append([0]*N)
    for i in range(1, N+1):
        for k in range(1, K+1):
            if i % 2:
                arr[k-1][i-1] += k + (i-1) * K
            else:
                arr[-k][i-1] += k + (i-1) * K
    res = ''
    for i in range(K):
        res += ' ' + str(sum(arr[i]))
    print('#{}{}'.format(test_case, res))
