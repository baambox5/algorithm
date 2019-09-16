arr = 'ABCDE'
N = len(arr)

for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            print(arr[i], arr[j], arr[k])


# 재귀
N, R = len(arr), 3
choose = []


def comb(k, s):
    if k == R:
        return
    else:
        for i in range(s, N):
            choose.append(arr[i])
            comb(k + 1, i + 1)
            choose.pop()


comb(0, 0)
