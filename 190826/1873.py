import sys
sys.stdin = open('1873.txt', 'r')


def d_move(char_in, t_x, t_y):
    if char_in == 'U':
        if t_x != 0 and arr[t_x-1][t_y] == '.':
            arr[t_x][t_y] = '.'
            t_x -= 1
            arr[t_x][t_y] = '^'            
        else:
            arr[t_x][t_y] = '^'
    elif char_in == 'D':
        if t_x != H-1 and arr[t_x+1][t_y] == '.':
            arr[t_x][t_y] = '.'
            t_x += 1
            arr[t_x][t_y] = 'v'            
        else:
            arr[t_x][t_y] = 'v'
    elif char_in == 'R':
        if t_y != W-1 and arr[t_x][t_y+1] == '.':
            arr[t_x][t_y] = '.'
            t_y += 1
            arr[t_x][t_y] = '>'            
        else:
            arr[t_x][t_y] = '>'
    else:
        if t_y != 0 and arr[t_x][t_y-1] == '.':
            arr[t_x][t_y] = '.'
            t_y -= 1
            arr[t_x][t_y] = '<'            
        else:
            arr[t_x][t_y] = '<'
    return t_x, t_y, arr[t_x][t_y]


def shoot(direction, t_x, t_y):
    if direction == '^':
        if t_x == 0 or arr[t_x-1][t_y] == '#':
            return
        elif arr[t_x-1][t_y] == '*':
            arr[t_x-1][t_y] = '.'
            return
        else:
            shoot(direction, t_x-1, t_y)
    elif direction == 'v':
        if t_x == H-1 or arr[t_x+1][t_y] == '#':
            return
        elif arr[t_x+1][t_y] == '*':
            arr[t_x+1][t_y] = '.'
            return
        else:
            shoot(direction, t_x+1, t_y)
    elif direction == '<':
        if t_y == 0 or arr[t_x][t_y-1] == '#':
            return
        elif arr[t_x][t_y-1] == '*':
            arr[t_x][t_y-1] = '.'
            return
        else:
            shoot(direction, t_x, t_y-1)
    else:
        if t_y == W-1 or arr[t_x][t_y+1] == '#':
            return
        elif arr[t_x][t_y+1] == '*':
            arr[t_x][t_y+1] = '.'
            return
        else:
            shoot(direction, t_x, t_y+1)
            

for test_case in range(1, int(input()) + 1):
    H, W = map(int, input().split())
    arr = [[] for _ in range(H)]
    for i in range(H):
        for char in input():
            arr[i] += [char]
    input()
    for i in range(H):
        for j in range(W):
            if arr[i][j] == '<' or arr[i][j] == '>' or arr[i][j] == '^' or arr[i][j] == 'v':
                x, y = i, j
                d_tank = arr[i][j]
    for char in input():
        if char == 'U' or char == 'D' or char == 'L' or char == 'R':
            x, y, d_tank = d_move(char, x, y)
        else:
            shoot(d_tank, x, y)
    print('#{}'.format(test_case), end=' ')
    for i in range(H):
        for j in range(W):
            print(arr[i][j], end='')
        print()