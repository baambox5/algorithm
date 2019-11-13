import sys
sys.stdin = open('home_security.txt', 'r')


for test_case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = []
    for _ in range(N):
        arr += [input().split()]
    max_count = 1
    for k in range(1, N + 1):
        cost = 2 * k * (k + 1) + 1
        for i in range(N):
            for j in range(N):
                sum_house = 0
                for s in range(k + 1):
                    for l in range(2 * s + 1):
                        x = i+l-s
                        y = j-k+s
                        if 0 <= x < N and 0 <= y < N:
                            if arr[x][y] == '1':
                                sum_house += 1
                for s in range(k - 1, -1, -1):
                    for l in range(2 * s, -1, -1):
                        x = i+s-l
                        y = j+k-s
                        if 0 <= x < N and 0 <= y < N:
                            if arr[x][y] == '1':
                                sum_house += 1
                if sum_house * M >= cost and sum_house > max_count:
                    max_count = sum_house
    print('#{} {}'.format(test_case, max_count))
