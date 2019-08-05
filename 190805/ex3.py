arr = [[9, 20, 2, 18, 11],
       [19, 1, 25, 3, 21],
       [8, 24, 10, 17, 7],
       [15, 4, 16, 5, 6],
       [12, 13, 22, 23, 14]
       ]
N, M = len(arr), len(arr[0])
row = 0
column = 0
for i in range(N):
    for rj in range(M-1, -1, -1):
        for j in range(M):
            print(arr[row][column])

    row = (row + ((i+1) % 2)) * (-1)

