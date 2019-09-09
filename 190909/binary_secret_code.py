import sys
sys.stdin = open('binary_secret_code.txt', 'r')

code = {0: '0001101', 1: '0011001', 2: '0010011', 3: '0111101', 4: '0100011', 5: '0110001', 6: '0101111',
        7: '0111011', 8: '0110111', 9: '0001011'}
for test_case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    str_in = []
    for _ in range(N):
        str_in += [input()]
    res = []
    row_idx = 0
    column_idx = 0
    for i in range(N - 4):
        for j in range(M - 52):
            if str_in[i][j] == '1':
                row_idx = i
                column_idx = j - 3
                break
        if row_idx:
            break
    i = column_idx
    count = 0
    while i < column_idx + 60:
        temp = ''
        for j in range(i, i + 7):
            temp += str_in[row_idx][j]
        for j in range(10):
            if code[j] == temp:
                res += [j]
                i += 6
                break
        else:
            if res:
                i = column_idx + count
                res = []
                count += 1
        if len(res) == 8:
            break
        i += 1
    odd = res[0] + res[2] + res[4] + res[6]
    even = res[1] + res[3] + res[5] + res[7]
    if (odd * 3 + even) % 10:
        print('#{} {}'.format(test_case, 0))
    else:
        print('#{} {}'.format(test_case, odd + even))
