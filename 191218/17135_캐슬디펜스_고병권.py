import sys
sys.stdin = open('castle_defense.txt', 'r')
from collections import deque
import copy


def defense():
    global max_count, enemy_count
    count = 0
    copy_position = copy.deepcopy(enemy_position)
    enemy = enemy_count
    attack = set()
    copy_arr = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            copy_arr[i][j] = arr[i][j]
    while enemy > 0:
        attack.clear()
        for archer in archers:
            Q = deque()
            visit = {}
            Q.append((N - 1, archer, 1))
            visit[(N - 1, archer)] = 1
            while Q:
                x, y, d = Q.popleft()
                if d > D:
                    break
                if copy_arr[x][y] == '1':
                    attack.add((x, y))
                    break
                for dx, dy in delta:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx and 0 <= ny < M and not visit.get((nx, ny)):
                        Q.append((nx, ny, d + 1))
                        visit[(nx, ny)] = 1
        for x, y in attack:
            copy_arr[x][y] = '0'
            enemy -= 1
            count += 1
            copy_position.discard((x, y))
        temp = set()
        for x, y in copy_position:
            copy_arr[x][y] = '0'
            if x == N - 1:
                enemy -= 1
            else:
                copy_arr[x + 1][y] = '1'
                temp.add((x + 1, y))
        copy_position = temp
    if max_count < count:
        max_count = count


def castle(k, s):
    if k == 3:
        defense()
    else:
        for p in range(s, M):
            archers[k] = p
            castle(k + 1, p + 1)


N, M, D = map(int, input().split())
enemy_position = set()
delta = ((0, -1), (-1, 0), (0, 1))
arr = []
enemy_count = 0
max_count = 0
archers = [0] * 3
for i in range(N):
    arr += [input().split()]
    for j in range(M):
        if arr[i][j] == '1':
            enemy_position.add((i, j))
            enemy_count += 1
if enemy_count:
    castle(0, 0)
print(max_count)
