import sys
sys.stdin = open('7964.txt', 'r')

for test_case in range(1, int(input()) + 1):
    N, M = tuple(map(int, input().split()))
    arr = input().split()
    position = -1
    count = 0
    while position < N:
        for i in range(position + M, position, -1):
            if arr[i] == '1':
                position = i
                break
        else:
            position += M
            count += 1
        if position + M >= N:
            break
    print(count)
