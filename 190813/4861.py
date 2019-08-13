import sys
sys.stdin = open('4861.txt', 'r')

for test_case in range(1, int(input()) + 1):
    # 입력 받기
    N, M = tuple(map(int, input().split()))
    arr = []
    res = ''
    # 한줄씩 입력 받음과 동시에 체크
    for i in range(N):
        arr += [input()]
        for j in range(N - M + 1):
            for k in range(M // 2):
                if arr[i][j+k] != arr[i][j-k+(M-N)-1]:
                    break
            else:
                res = arr[i][j:j+M]
                break
    # 만약 가로축에서 발견했으면 세로축 검사는 그냥 넘어감
    if not res:
        for j in range(N):
            for i in range(N - M + 1):
                for k in range(M // 2):
                    if arr[i+k][j] != arr[i-k+(M-N)-1][j]:
                        break
                else:
                    for l in range(M):
                        res += arr[i+l][j]
                    break
            if res:
                break
    print('#{} {}'.format(test_case, res))

