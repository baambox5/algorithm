import sys
sys.stdin = open('4836.txt', 'r')

for test_case in range(1, int(input()) + 1):
    N = int(input())
    arr = []
    count = 0
    for i in range(10):
        arr.append([0]*10)
    for i in range(N):
        area = tuple(map(int, input().split()))
        for j in range(area[0], area[2]+1):
            for k in range(area[1], area[3]+1):
                if arr[j][k] == 0:
                    arr[j][k] = area[-1]
                else:
                    arr[j][k] = 3
                    count += 1
    print('#{} {}'.format(test_case, count))



