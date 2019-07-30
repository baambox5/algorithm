import sys
sys.stdin = open('input_4831.txt', 'r')

for test_case in range(1, int(input())+1):
    K, N, M = tuple(map(int, input().split()))
    arr = list(map(int, input().split()))
    station = [0] * (N+1)
    count = 0
    position = 0
    for i in arr:
        station[i] += 1
    while position < N:
        for i in range(K+position, position, -1):
            if station[i]:
                count += 1
                position = i
                break
        else:
            count = 0
            break
        if (position+K) >= N:
            break
    print('#{} {}'.format(test_case, count))
