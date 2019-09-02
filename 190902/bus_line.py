import sys
sys.stdin = open('bus_line.txt', 'r')

# for test_case in range(1, int(input()) + 1):
#     arr = [0] * 5001
#     for _ in range(int(input())):
#         a, b = map(int, input().split())
#         for i in range(a, b + 1):
#             arr[i] += 1
#     print('#{}'.format(test_case), end=' ')
#     for _ in range(int(input())):
#         print(arr[int(input())], end=' ')
#     print()


for test_case in range(1, int(input()) + 1):
    arr = {}
    for _ in range(int(input())):
        a, b = map(int, input().split())
        for i in range(a, b + 1):
            if i not in arr:
                arr[i] = 1
            else:
                arr[i] += 1
    print('#{}'.format(test_case), end=' ')
    for _ in range(int(input())):
        C = int(input())
        if C in arr:
            print(arr[C], end=' ')
        else:
            print(0, end=' ')
    print()
