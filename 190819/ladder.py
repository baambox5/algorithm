import sys
sys.stdin = open('ladder.txt', 'r')

for _ in range(10, 11):
    test_case = input()
    arr = [[] for _ in range(100)]
    position_y = 0
    for i in range(100):
        arr[i] = input().split()
    for j in range(100):
        if arr[0][j]:
            position_y = j
            for i in range(1, 100):
                for k in range(1, 100):
                    if position_y == 0:
                        if not arr[i][position_y + k]:
                            position_y += k - 1
                            break
                    elif position_y == 99:
                        if not arr[i][position_y - k]:
                            position_y += 1 - k
                            break
                    else:
                        if arr[i][position_y + k]:
            else:
                if arr[99][position_y] == 2:
                    res = j
                    break

