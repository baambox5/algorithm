import sys
sys.stdin = open('reading_column.txt', 'r')

for test_case in range(1, int(input()) + 1):
    arr = []
    len_arr = []
    for i in range(5):
        arr += [input()]
        len_arr += [len(arr[i])]
    print('#{}'.format(test_case), end=' ')
    for j in range(15):
        for i in range(5):
            if j < len_arr[i]:
                print(arr[i][j], end='')
    print()
