import sys
sys.stdin = open('1974.txt', 'r')

for test_case in range(1, int(input()) + 1):
    arr = []
    for _ in range(9):
        arr.append(list(map(int, input().split())))
    error = 0
    for i in range(9):
        row = [0] * 10
        column = [0] * 10
        for j in range(9):
            row[arr[i][j]] += 1
            column[arr[j][i]] += 1
            if row[arr[i][j]] > 1 or column[arr[j][i]] > 1:
                error = 1
                break
            if not i % 3 and not j % 3:
                box = [0] * 10
                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        box[arr[k][l]] += 1
                        if box[arr[k][l]] > 1:
                            error = 1
                            break
                    if error:
                        break
        if error:
            break
    if error:
        print('#{} {}'.format(test_case, 0))
    else:
        print('#{} {}'.format(test_case, 1))
