import sys
sys.stdin = open('17136.txt', 'r')

arr = []
for _ in range(10):
    arr.append(input().split())
copy_arr = [[0] * 10 for _ in range(10)]
visit = [[0] * 10 for _ in range(10)]
for i in range(10):
    for j in range(10):
        if arr[i][j] == '1' and not copy_arr[i][j]:
            for k in range(i, 10):
                for l in range(j, 10):
                    if arr[k][l] == '1':
                        copy_arr[k][j] += 1
                    else:
                        break
                if arr[k][j] == '0':
                    break
min_count = 0
squares = [5, 5, 5, 5, 5]
for k in range(5, 0, -1):
    for i in range(10):
        for j in range(10):
            if copy_arr[i][j] >= k and not visit[i][j]:
                for l in range(1, k):
                    if i + l == 10 or copy_arr[i + l][j] < k:
                        break
                else:
                    for s in range(i, i + k):
                        for n in range(1, k):
                            if j - n == -1 or not copy_arr[s][j - n]:
                                break
                            else:
                                copy_arr[s][j - n] -= k
                        for p in range(j, j + k):
                            copy_arr[s][p] = k
                            visit[s][p] = 1
                    min_count += 1
                    squares[k-1] -= 1
for square in squares:
    if square < 0:
        print(-1)
        break
else:
     print(min_count)