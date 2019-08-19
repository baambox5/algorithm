import sys
sys.stdin = open('7985.txt', 'r')

for test_case in range(1, int(input()) + 1):
    depth = int(input())
    num_in = list(map(int, input().split()))
    len_num = len(num_in)
    print('#{} '.format(test_case), end='')
    for i in range(depth):
        for j in range(2 ** i):
            print(num_in[(len_num // 2 ** (i+1)) + (2**(depth-i)) * j], end=' ')
        print()

    