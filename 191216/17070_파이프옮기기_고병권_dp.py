import sys
sys.stdin = open('move_pipe.txt', 'r')


def pipe(x, y, state):
    if house[x][y] == '1':
        return 0
    if pipe_memo[x][y][state] >= 0:
        return pipe_memo[x][y][state]
    if x == N - 1 and y == N - 1:
        pipe_memo[x][y][state] = 1
        return 1
    sum_value = 0
    if state == 0:
        if y < N - 1:
            sum_value += pipe(x, y + 1, 0)
    elif state == 1:
        if y < N - 1:
            sum_value += pipe(x, y + 1, 0)
        if x < N - 1:
            sum_value += pipe(x + 1, y, 2)
    else:
        if x < N - 1:
            sum_value += pipe(x + 1, y, 2)
    if x < N - 1 and y < N - 1:
        if house[x + 1][y] != '1' and house[x][y + 1] != '1':
            sum_value += pipe(x + 1, y + 1, 1)
    pipe_memo[x][y][state] = sum_value
    return sum_value


N = int(input())
house = [input().split() for _ in range(N)]
pipe_memo = [[[-1, -1, -1] for _ in range(N)] for _ in range(N)]
res = pipe(0, 1, 0)
print(res)
