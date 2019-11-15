import sys
sys.stdin = open('stem_cell.txt', 'r')

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
for test_case in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    cell = {}
    for i in range(N):
        arr = list(map(int, input().split()))
        for j in range(M):
            if arr[j]:
                cell[(i, j)] = [arr[j], arr[j], 0, 1]
    t = 0
    dead_cell = {}
    while t < K:
        add_cell = {}
        for position, value in cell.items():
            if value[0]:
                add_cell[position] = [value[0] - 1, value[1], value[2], 1]
            else:
                if value[3]:
                    x, y = position
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if (nx, ny) in dead_cell or (nx, ny) in cell:
                            continue
                        if (nx, ny) in add_cell:
                            if add_cell[(nx, ny)][1] < value[1] and add_cell[(nx, ny)][2] == t:
                                add_cell[(nx, ny)] = [value[1], value[1], t, 1]
                        else:
                            add_cell[(nx, ny)] = [value[1], value[1], t, 1]
                    if value[1] - 1:
                        add_cell[(x, y)] = [0, value[1] - 1, value[2], 0]
                    else:
                        dead_cell[position] = 0
                else:
                    if value[1] - 1:
                        add_cell[position] = [0, value[1] - 1, value[2], 0]
                    else:
                        dead_cell[position] = 0
        cell = add_cell
        t += 1
    print('#{} {}'.format(test_case, len(cell)))
