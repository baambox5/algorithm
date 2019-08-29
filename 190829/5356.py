import sys
sys.stdin = open('5356.txt', 'r')

for test_case in range(1, int(input()) + 1):
    arr = []
    len_list = []
    for i in range(5):
        arr += [input()]
        len_list += [len(arr[i])]
    print('#{}'.format(test_case), end=' ')
    j = 0
    while j < 15:
        for i in range(5):
            if len_list[i] <= j:
                continue
            print('{}'.format(arr[i][j]), end='')
        if len_list[0] <= j and len_list[1] <= j and len_list[2] <= j and len_list[3] <= j and len_list[4] <= j:
            break 
        j += 1
    print()
        