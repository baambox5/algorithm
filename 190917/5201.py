import sys
sys.stdin = open('5201.txt', 'r')

for test_case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    w = []
    for i in input().split():
        if w:
            temp = int(i)
            for j in range(len(w)):
                if int(i) > w[j]:
                    w[j], temp = temp, w[j]
            w += [temp]
        else:
            w += [int(i)]
    t = []
    for i in input().split():
        if t:
            temp = int(i)
            for j in range(len(t)):
                if int(i) > t[j]:
                    t[j], temp = temp, t[j]
            t += [temp]
        else:
            t += [int(i)]
    select = [0] * M
    weight = 0
    for i in w:
        for j in range(M):
            if i > t[j]:
                break
            elif not select[j]:
                select[j] = 1
                weight += i
                break
    print('#{} {}'.format(test_case, weight))
