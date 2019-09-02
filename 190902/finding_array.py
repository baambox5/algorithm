import sys
sys.stdin = open('finding_array.txt', 'r')


def dfs(x, y, x_count, y_count):
    global res_x, res_y
    visit[x][y] += 1
    if y != N-1 and arr[x][y+1] and not visit[x][y+1]:
        dfs(x, y+1, x_count, y_count + 1)
    else:
        if res_y < y_count:
            res_y = y_count
    if x != N-1 and arr[x+1][y] and not visit[x+1][y]:
        dfs(x+1, y, x_count + 1, y_count)
    else:
        if res_x < x_count:
            res_x = x_count


def merge_sort(a):
    if len(a) <= 1:
        return a
    else:
        mid = len(a) // 2
        left = a[:mid]
        right = a[mid:]
        left = merge_sort(left)
        right = merge_sort(right)
        return merge(left, right)


def merge(left, right):
    result = []
    while left and right:
        if left[0][0]*left[0][1] < right[0][0]*right[0][1]:
            result.append(left.pop(0))
        elif left[0][0]*left[0][1] == right[0][0]*right[0][1]:
            if left[0][0] < right[0][0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        else:
            result.append(right.pop(0))
    if left:
        result.extend(left)
    if right:
        result.extend(right)
    return result


for test_case in range(1, int(input()) + 1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    visit = [[0] * N for _ in range(N)]
    count = 0
    temp = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] and not visit[i][j]:
                res_x, res_y = 0, 0
                count += 1
                dfs(i, j, 1, 1)
                temp.append((res_x, res_y))
    res = merge_sort(temp)
    print('#{} {}'.format(test_case, count), end=' ')
    for x, y in res:
        print('{} {}'.format(x, y), end=' ')
    print()
