import sys
sys.stdin = open('input.txt', 'r')

for test_case in range(1, 11):
    test_number = input()
    arr = [[0]*100] * 100
    max_sum = 0
    sum_diag = 0
    sum_diag2 = 0
    for i in range(100):
        arr[i] = list(map(int, input().split()))
    for i in range(100):
        sum_row = 0
        sum_column = 0
        sum_diag += arr[i][i]
        sum_diag2 += arr[-i - 1][i]
        for j in range(100):
            sum_row += arr[i][j]
            sum_column += arr[j][i]
        if sum_row > max_sum:
            max_sum = sum_row
        if sum_column > max_sum:
            max_sum = sum_column
    if sum_diag > max_sum:
        max_sum = sum_diag
    if sum_diag2 > max_sum:
        max_sum = sum_diag2
    print('#{} {}'.format(test_case, max_sum))

