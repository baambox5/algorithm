import sys
sys.stdin = open('4869.txt', 'r')


def recur(num):
    if num <= 1:
        return 1
    return num * recur(num-1)


for test_case in range(1, int(input()) + 1):
    N = int(input())
    ac_max = N // 20
    b_max = N // 10
    res = 0
    for a in range(ac_max + 1):
        for c in range(ac_max + 1):
            for b in range(b_max + 1):
                if (2*a + b + 2*c) > b_max:
                    break
                elif (2*a + b + 2*c) == b_max:
                    res += recur(a+b+c) // (recur(a)*recur(b)*recur(c))
    print('#{} {}'.format(test_case, res))
