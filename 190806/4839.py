import sys
sys.stdin = open('4839.txt', 'r')

for test_case in range(1, int(input()) + 1):
    P, A, B = tuple(map(int, input().split()))
    al = 1
    ar = P
    bl = 1
    br = P
    winner = 0
    while winner == 0:
        c = (al+ar) // 2
        if A > c:
            al = c
        else:
            ar = c
        if A == c:
            winner = 'A'
        c = (bl+br) // 2
        if B > c:
            bl = c
        else:
            br = c
        if B == c:
            if winner == 'A':
                winner = 0
                break
            else:
                winner = 'B'
    print('#{} {}'.format(test_case, winner))