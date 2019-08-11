import sys
sys.stdin = open('input.txt', 'r')

arr = []
count = 0
inst = []

# 입력 받기
for _ in range(5):
    arr.append(input().split())
for _ in range(5):
    inst += input().split()

# 사회자가 부르는 숫자를 하나하나 체크
for num in inst:
    # 있는 위치를 찾아서 값을 0으로 바꿔주고 부른 횟수를 1 추가
    for i in range(5):
        for j in range(5):
            if num == arr[i][j]:
                arr[i][j] = 0
                count += 1
    # 행, 열, 대각선에서 행렬의 요소값이 0일때만 체크
    diag_bingo = 0
    rediag_bingo = 0
    bingo = 0
    for i in range(5):
        row_bingo = 0
        column_bingo = 0
        if not arr[i][i]:
            diag_bingo += 1
        if not arr[-i-1][i]:
            rediag_bingo += 1
        for j in range(5):
            if not arr[i][j]:
                row_bingo += 1
            if not arr[j][i]:
                column_bingo += 1
        # 체크한 갯수가 5일 경우 한줄이 전부 불러진 것이므로 bingo변수의 값 1 추가
        if row_bingo == 5:
            bingo += 1
        if column_bingo == 5:
            bingo += 1
    if diag_bingo == 5:
        bingo += 1
    if rediag_bingo == 5:
        bingo += 1
    # bingo 변수값이 3이상일 경우 빙고이므로 반복문 종료
    if bingo >= 3:
        break
print(count)

