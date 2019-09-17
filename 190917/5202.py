import sys
sys.stdin = open('5202.txt', 'r')

for test_case in range(1, int(input()) + 1):
    N = int(input())
    start = []
    end = []
    for _ in range(N):
        s, e = map(int, input().split())
        if end:
            temp_s = s
            temp_e = e
            for i in range(len(end)):
                if e < end[i]:
                    temp_s, start[i] = start[i], temp_s
                    temp_e, end[i] = end[i], temp_e
            start += [temp_s]
            end += [temp_e]
        else:
            start += [s]
            end += [e]
    count = 0
    time = 0
    for i in range(N):
        if start[i] >= time:
            time = end[i]
            count += 1
    print('#{} {}'.format(test_case, count))
