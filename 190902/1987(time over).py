import sys
sys.stdin = open('1987.txt', 'r')


def dfs(x, y, count, a):
    global max_count
    for i in range(4):
        x_d = x + x_delta[i]
        y_d = y + y_delta[i]  
        if 0 <= x_d <= R-1 and 0 <= y_d <= C-1:
            if not a[ord(arr[x_d][y_d])-65]:
                a[ord(arr[x_d][y_d])-65] += 1
                dfs(x_d, y_d, count + 1, a)
                a[ord(arr[x_d][y_d])-65] -= 1
    if count > max_count:
        max_count = count

R, C = map(int, input().split())
arr = []
ascii_alpha = [0] * 26
for _ in range(R):
    arr.append(input())
x_delta = [-1, 0, 1, 0]
y_delta = [0, -1, 0, 1]
max_count = 1
ascii_alpha[ord(arr[0][0])-65] += 1
dfs(0, 0, 1, ascii_alpha)
print(max_count)