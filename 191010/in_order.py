import sys
sys.stdin = open('in_order.txt', 'r')


def in_order(n):
    if n:
        in_order(arr[n][0])
        print(char[n], end='')
        in_order(arr[n][1])


for test_case in range(1, 11):
    N = int(input())
    char = [''] * (N + 1)
    arr = [[0] * 2 for _ in range(N + 1)]
    for i in range(N):
        in_str = input().split()
        n = int(in_str[0])
        char[n] = in_str[1]
        if len(in_str) != 2:
            arr[n][0] = int(in_str[2])
            if len(in_str) != 3:
                arr[n][1] = int(in_str[3])
    print('#{}'.format(test_case), end=' ')
    in_order(1)
    print()
