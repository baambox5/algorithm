import sys
sys.stdin = open('pool.txt', 'r')


def perm(k, cost):
    global min_value
    if k >= 12:
        if min_value > cost:
            min_value = cost
        return
    elif cost >= min_value:
        return
    else:
        if plan[k]:
            perm(k + 1, cost + ticket[0] * plan[k])
            perm(k + 1, cost + ticket[1])
            perm(k + 3, cost + ticket[2])
            perm(k + 12, cost + ticket[3])
        else:
            perm(k + 1, cost)


for test_case in range(1, int(input()) + 1):
    ticket = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    min_value = 1000000
    perm(0, 0)
    print('#{} {}'.format(test_case, min_value))
