arr = [3, 6, -2, 7, -3, 1, -5, -1, 5, 4]
N = len(arr)
for subset in range(1 << N):
    sum_subset = 0
    for i in range(N):
        if subset & (1 << i):
            sum_subset += arr[i]
    if sum_subset == 0:
        for i in range(N):
            if subset & (1 << i):
                print(arr[i], end=' ')
        print()
