import sys
sys.stdin = open('1979.txt', 'r')

for test_case in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(input().split())
    res = 0    
    row_count = 0
    column_count = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '1':
                row_count += 1
            if arr[j][i] == '1':
                column_count += 1
            if j == N-1 or arr[i][j] == '0':
                if row_count == K:
                    res += 1
                row_count = 0
            if j == N-1 or arr[j][i] == '0':
                if column_count == K:
                    res += 1                
                column_count = 0
    print('#{} {}'.format(test_case, res))
        
