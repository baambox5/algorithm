import sys
sys.stdin = open('move_pipe.txt', 'r')


def pipe(x, y, state):
    global count
    if x == N - 1 and y == N - 1:
        count += 1
        return
    for dx, dy, next_state in delta[state]:
        if next_state == 0:
            ny = y + dy
            if y < N - 1 and house[x][ny] != '1':
                pipe(x, ny, 0)
        elif next_state == 1:
            nx = x + dx
            ny = y + dy
            if x < N - 1 and y < N - 1:
                if house[nx][y] != '1' and house[x][ny] != '1' and house[nx][ny] != '1':
                    pipe(nx, ny, 1)
        else:
            nx = x + dx
            if x < N - 1 and house[nx][y] != '1':
                pipe(nx, y, 2)


N = int(input())
delta = {0: [(0, 1, 0), (1, 1, 1)], 1: [(0, 1, 0), (1, 1, 1), (1, 0, 2)], 2: [(1, 1, 1), (1, 0, 2)]}
house = [input().split() for _ in range(N)]
count = 0
pipe(0, 1, 0)
print(count)
