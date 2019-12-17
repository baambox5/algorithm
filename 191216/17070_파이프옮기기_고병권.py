import sys
sys.stdin = open('move_pipe.txt', 'r')


def pipe(x, y, state):
    print(x, y, state, pipe_memo[x][y][state])
    if pipe_memo[x][y][state]:
        print(write)
        return pipe_memo[x][y][state]
    if house[x][y] == '1':
        return 0
    sum_value = 0
    write.append((x, y, state))
    if state == 0:
        if y < N - 1:
            sum_value += pipe(x, y + 1, 0)
    elif state == 1:
        if 1 <= x and 1 <= y:
            if house[x - 1][y] == '1' or house[x][y - 1] == '1':
                return 0
        if y < N - 1:
            sum_value += pipe(x, y + 1, 0)
        if x < N - 1:
            sum_value += pipe(x + 1, y, 2)
    else:
        if x < N - 1:
            sum_value += pipe(x + 1, y, 2)
    if x < N - 1 and y < N - 1:
        sum_value += pipe(x + 1, y + 1, 1)
    if sum_value:
        pipe_memo[x][y][state] = 1
    write.pop()
    return sum_value


N = int(input())
house = [input().split() for _ in range(N)]
pipe_memo = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]
pipe_memo[N-1][N-1][0] = 1
pipe_memo[N-1][N-1][1] = 1
pipe_memo[N-1][N-1][2] = 1
write = []
res = pipe(0, 1, 0)
print(pipe_memo)
print(res)
