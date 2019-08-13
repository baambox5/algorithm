import sys
sys.stdin = open('1946.txt', 'r')

for test_case in range(1, int(input()) + 1):
    N = int(input())
    k = 0
    print('#{}'.format(test_case))
    for i in range(N):
        key, value = input().split()
        for j in range(int(value)):
            print('{}'.format(key), end='')
            k += 1
            if k >= 10:
                print()
                k = 0
    print()




