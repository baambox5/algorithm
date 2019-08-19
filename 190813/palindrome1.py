import sys
sys.stdin = open('palindrome1.txt', 'r')

for test_case in range(1, 11):
    M = int(input())
    count = 0
    arr = []
    half_M = M // 2
    # 입력 받기
    for _ in range(8):
        arr += [input()]
    for i in range(8):
        # 8 - M + 1 만큼 확인
        for j in range(9 - M):
            row_count = 0
            column_count = 0
            e = j + M - 1
            # 가로, 세로 둘 다 동시에 확인
            for k in range(half_M):
                if arr[i][j+k] == arr[i][e-k]:
                    row_count += 1
                if arr[j+k][i] == arr[e-k][i]:
                    column_count += 1
            if row_count == half_M:
                count += 1
            if column_count == half_M:
                count += 1
    # 만약 회문 길이가 1인 경우
    if not half_M:
        count //= 2
    print('#{} {}'.format(test_case, count))
