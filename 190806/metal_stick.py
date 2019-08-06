import sys
sys.stdin = open('metal_stick.txt', 'r')

for test_case in range(1, int(input()) + 1):
    num_screw = int(input())
    arr = input().split()
    max_idx = 0
    for i in range(0, num_screw*2, 2):
        max_count = 0
        for j in range(i, num_screw*2, 2):
            count = 0
            for k in range(i, num_screw*2, 2):
                if arr[j] != arr[k+1]:
                    count += 1
            if count > max_count:
                max_count = count
                max_idx = j
        arr[i], arr[i+1], arr[max_idx], arr[max_idx+1] = arr[max_idx], arr[max_idx+1], arr[i], arr[i+1]
    res = ''
    for i in arr:
        res += ' ' + i
    print('#{}{}'.format(test_case, res))
