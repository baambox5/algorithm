import sys
sys.stdin = open('secret_code_scan.txt', 'r')

code = {0: '0001101', 1: '0011001', 2: '0010011', 3: '0111101', 4: '0100011', 5: '0110001', 6: '0101111',
        7: '0111011', 8: '0110111', 9: '0001011'}
for test_case in range(15, int(input()) + 1):
    N, M = map(int, input().split())
    str_in = ''
    column_idx = 0
    zero_list = []
    for _ in range(N):
        str_in = input()
        for i in range(M):
            if str_in != '0':
                column_idx = i
                break
        if column_idx:
            i = column_idx
            while i < M:
                for j in range():

                i += 1

