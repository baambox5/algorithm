import sys
sys.stdin = open('othello.txt', 'r')


def dfs(x, y, d_x, d_y):
    global color, flag
    if color == arr[x][y]:
        flag = 1
        return
    elif arr[x][y] == 0:
        return
    elif 1 <= x + d_x <= N and 1 <= y + d_y <= N:
        if color == 1 and arr[x][y] == 2 and x != 0:
            temp.append((x, y))
            dfs(x + d_x, y + d_y, d_x, d_y)
        elif color == 2 and arr[x][y] == 1:
            temp.append((x, y))
            dfs(x + d_x, y + d_y, d_x, d_y)
    else:
        return


d_row = [-1, -1, -1, 0, 0, 1, 1, 1]
d_column = [-1, 0, 1, -1, 1, -1, 0, 1]
for test_case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = [[0] * (N + 1) for _ in range(N + 1)]
    arr[N // 2][N // 2], arr[N // 2 + 1][N // 2 + 1] = 2, 2
    arr[N // 2][N // 2 + 1], arr[N // 2 + 1][N // 2] = 1, 1
    for _ in range(M):
        a, b, color = map(int, input().split())
        arr[a][b] = color
        for i in range(8):
            row = a + d_row[i]
            column = b + d_column[i]
            if 1 <= row <= N and 1 <= column <= N:
                flag = 0
                temp = []
                dfs(row, column, d_row[i], d_column[i])
                if flag:
                    for x_c, y_c in temp:
                        arr[x_c][y_c] = color
    b_count = 0
    w_count = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if arr[i][j] == 1:
                b_count += 1
            elif arr[i][j] == 2:
                w_count += 1
    print('#{} {} {}'.format(test_case, b_count, w_count))
