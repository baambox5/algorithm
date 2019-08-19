import sys
sys.stdin = open('8016.txt', 'r')

for test_case in range(1, int(input()) + 1):
    line = int(input())
    m = 2 * (line - 1)
    bn = 1 + line * m
    N = bn - m
    K = bn + m
    print('#{} {} {}'.format(test_case, N, K))
