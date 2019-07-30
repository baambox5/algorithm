import sys
sys.stdin = open('input_4835.txt', 'r')

for test_case in range(1, int(input())+1):
    N, M = tuple(map(int, input().split()))
    arr = list(map(int, input().split()))
    for i in range(N-M+1):
        result = 0
        for j in range(M):
            result += arr[i+j]
        if i:
            if result > max_value:
                max_value = result
            if result < min_value:
                min_value = result
        else:
            max_value = result
            min_value = result
    print('#{} {}'.format(test_case, max_value-min_value))
