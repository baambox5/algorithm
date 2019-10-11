import sys
sys.stdin = open('5174.txt', 'r')


def find(n):
    global count
    if n:
        count += 1
        find(arr[n][0])
        find(arr[n][1])


for test_case in range(1, int(input()) + 1):
    E, N = map(int, input().split())
    arr = [[0] * 2 for _ in range(E + 2)]
    get_str = list(map(int, input().split()))
    for i in range(E):
        if not arr[get_str[i*2]][0]:
            arr[get_str[i*2]][0] = get_str[i*2+1]
        else:
            arr[get_str[i*2]][1] = get_str[i*2+1]
    count = 0
    find(N)
    print('#{} {}'.format(test_case, count))
