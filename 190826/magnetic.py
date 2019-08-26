import sys
sys.stdin = open('magnetic.txt', 'r')

for test_case in range(1, 11):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(input().split())
    count = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '1':
                for k in range(i+1, N):
                    if arr[k][j] == '1':
                        break
                    elif arr[k][j] == '2':
                        count += 1
                        break
    print('#{} {}'.format(test_case, count))
