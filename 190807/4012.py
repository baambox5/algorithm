import sys
sys.stdin = open('4012.txt', 'r')

for test_case in range(1, int(input())+1):
    N = int(input())
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))
    min_taste = 10000
    diff = 0
    for i in range(1 << (N-1)):
        count = 0
        A_idx = []
        B_idx = []
        for j in range(N):
            if i & (1 << j):
                count += 1
                A_idx += [j]
            else:
                B_idx += [j]
        if count == N // 2:
            A_taste = 0
            B_taste = 0
            for k in range(0, count - 1):
                for l in range(1+k, count):
                    A_taste += arr[A_idx[k]][A_idx[l]] + arr[A_idx[l]][A_idx[k]]
                    B_taste += arr[B_idx[k]][B_idx[l]] + arr[B_idx[l]][B_idx[k]]
            diff = A_taste - B_taste
            if diff < 0:
                diff = -diff
            if min_taste > diff:
                min_taste = diff
    print('#{} {}'.format(test_case, min_taste))