import sys
sys.stdin = open('2628.txt', 'r')

# 종이 자르기
# 입력 받기
x, y = map(int, input().split())
n = int(input())
# 행과 열, 각각의 리스트에 0 저장해두기
cut_row = [0]
cut_column = [0]
# 입력 받음과 함께 정렬함.
for _ in range(n):
    # 입력 받기
    col, cutting_line = map(int, input().split())
    # 자르는 선이 가로인지 세로인지 확인해서
    if col:
        # 새로 입력 받은 것이 작을때 바꿔준다. 기존의 입력에 비해 입력값이 작을수록 for문이 많이 돔
        for i in range(len(cut_column)):
            if cutting_line < cut_column[i]:
                cut_column[i], cutting_line = cutting_line, cut_column[i]
        # 이 중에서 제일 큰 값도 저장
        cut_column.append(cutting_line)
    else:
        for i in range(len(cut_row)):
            if cutting_line < cut_row[i]:
                cut_row[i], cutting_line = cutting_line, cut_row[i]
        cut_row.append(cutting_line)
else:
    # 리스트 내에서 비교하기 위해 제일 큰 값도 넣어준다.
    cut_column.append(x)
    cut_row.append(y)
max_width = 0
# 가로, 세로 리스트의 요소들 사이의 차가 길이가 된다.
for i in range(1, len(cut_row)):
    row_length = cut_row[i] - cut_row[i - 1]
    for j in range(1, len(cut_column)):
        width = row_length * (cut_column[j] - cut_column[j - 1])
        if max_width < width:
            max_width = width
print(max_width)
