import sys
sys.stdin = open('5427.txt', 'r')
from collections import deque


for test_case in range(1, int(input()) + 1):
    M, N = map(int, input().split())
    arr = [[] for _ in range(N)]
    for i in range(N):
        for char in input():
            arr[i] += [char]

    fire = deque()
    human = deque()
    visit = [[0] * M for _ in range(N)]
    success = 0
    k = 0
    fire_count = 0

    for i in range(N):
        for j in range(M):
            if arr[i][j] == '*':
                fire.append((i, j))
                fire_count += 1
            elif arr[i][j] == '@':
                start_x, start_y = i, j    
    human.append((start_x, start_y, 0))
    visit[start_x][start_y] = 1

    while human:
        x, y, count = human.popleft()
        if count == k:
            f_count = 0
            for _ in range(fire_count):
                f_x, f_y = fire.popleft()                            
                if f_x != N-1 and arr[f_x+1][f_y] == '.':
                    arr[f_x+1][f_y] = '*'
                    fire.append((f_x+1, f_y))
                    f_count += 1
                if f_y != M-1 and arr[f_x][f_y+1] == '.':
                    arr[f_x][f_y+1] = '*'
                    fire.append((f_x, f_y+1))
                    f_count += 1
                if f_x != 0 and arr[f_x-1][f_y] == '.':
                    arr[f_x-1][f_y] = '*'
                    fire.append((f_x-1, f_y))
                    f_count += 1
                if f_y != 0 and arr[f_x][f_y-1] == '.':
                    arr[f_x][f_y-1] = '*'
                    fire.append((f_x, f_y-1))
                    f_count += 1
            else:
                fire_count = f_count
            k += 1

        if x == N-1 or x == 0 or y == M-1 or y == 0:
            success = 1
            break
        if x != N-1 and arr[x+1][y] == '.' and not visit[x+1][y]:
            visit[x+1][y] = 1
            human.append((x+1, y, count+1))
        if y != M-1 and arr[x][y+1] == '.' and not visit[x][y+1]:
            visit[x][y+1] = 1
            human.append((x, y+1, count+1))
        if x != 0 and arr[x-1][y] == '.' and not visit[x-1][y]:
            visit[x-1][y] = 1
            human.append((x-1, y, count+1))
        if y != 0 and arr[x][y-1] == '.' and not visit[x][y-1]:
            visit[x][y-1] = 1
            human.append((x, y-1, count+1))

    if success:
        print(count + 1)
    else:
        print('IMPOSSIBLE')
