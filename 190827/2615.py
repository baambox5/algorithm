import sys
sys.stdin = open('2615.txt', 'r')


def dfs(x, y, value, direction, count):
    global outer
    if count == 5:
        if direction == 8:
            if i != 0 and j != 0 and arr[i-1][j-1] == value:
                outer = 0
            else:
                outer = 1
        if direction == 3:
            if i != 18 and j != 0 and arr[i+1][j-1] == value:
                outer = 0
            else:
                outer = 1
        if direction == 5:
            if j != 0 and arr[i][j - 1] == value:
                outer = 0
            else:
                outer = 1
        if direction == 7:
            if i != 0 and arr[i - 1][j] == value:
                outer = 0
            else:
                outer = 1
    if count >= 6:
        outer = 0
    if x != 18:
        if y != 18 and arr[x+1][y+1] == value:
            if direction == 0 or direction == 8:
                dfs(x + 1, y + 1, value, 8, count + 1)
        if arr[x+1][y] == value:
            if direction == 0 or direction == 7:
                dfs(x + 1, y, value, 7, count + 1)
    if x != 0 and y != 18 and arr[x-1][y+1] == value:
        if direction == 0 or direction == 3:
            dfs(x - 1, y + 1, value, 3, count + 1)
    if y != 18 and arr[x][y + 1] == value:
        if direction == 0 or direction == 5:
            dfs(x, y + 1, value, 5, count + 1)


arr = []
flag = 1
res = 0
outer = 0
for _ in range(19):
    arr.append(list(map(int, input().split())))
visit = [[0] * 19 for _ in range(19)]
for i in range(19):
    for j in range(19):
        if arr[i][j] == 1 or arr[i][j] == 2:
            dfs(i, j, arr[i][j], 0, 1)
            if outer:
                flag = 0
                print(arr[i][j])
                print(i+1, j+1)
                break
            outer = 0
    if not flag:
        break
if flag:
    print(0)

