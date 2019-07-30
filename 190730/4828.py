import sys
sys.stdin = open('input_4828.txt', 'r')

for test_case in range(1, int(input())+1):
    len_number = int(input())
    arr = list(map(int, input().split()))
    min_value = arr[0]
    max_value = arr[0]
    for i in range(1, len_number):
        if arr[i] > max_value:
            max_value = arr[i]
        if arr[i] < min_value:
            min_value = arr[i]
    print('#{} {}'.format(test_case, max_value-min_value))
