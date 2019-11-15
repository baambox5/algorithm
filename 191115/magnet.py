import sys
sys.stdin = open('magnet.txt', 'r')
from collections import deque


def check(t, d, c):
    if t == 1:
        if m1[2] != m2[-2] and not c:
            check(t + 1, d * (-1), 1)
        if d == 1:
            m1.appendleft(m1.pop())
        else:
            m1.append(m1.popleft())
    elif t == 4:
        if m4[-2] != m3[2] and not c:
            check(t - 1, d * (-1), 4)
        if d == 1:
            m4.appendleft(m4.pop())
        else:
            m4.append(m4.popleft())
    elif t == 2:
        if m2[2] != m3[-2] and (not c or c == 1):
            check(t + 1, d * (-1), 2)
        if m2[-2] != m1[2] and (not c or c == 3):
            check(t - 1, d * (-1), 2)
        if d == 1:
            m2.appendleft(m2.pop())
        else:
            m2.append(m2.popleft())
    else:
        if m3[2] != m4[-2] and (not c or c == 2):
            check(t + 1, d * (-1), 3)
        if m3[-2] != m2[2] and (not c or c == 4):
            check(t - 1, d * (-1), 3)
        if d == 1:
            m3.appendleft(m3.pop())
        else:
            m3.append(m3.popleft())


for test_case in range(1, int(input()) + 1):
    m1, m2, m3, m4 = deque(), deque(), deque(), deque()
    K = int(input())
    for _ in range(4):
        if m1:
            if m2:
                if m3:
                    m4 += list(map(int, input().split()))
                else:
                    m3 += list(map(int, input().split()))
            else:
                m2 += list(map(int, input().split()))
        else:
            m1 += list(map(int, input().split()))
    for _ in range(K):
        touch, direction = map(int, input().split())
        check(touch, direction, 0)
    result = m1[0] + 2 * m2[0] + 4 * m3[0] + 8 * m4[0]
    print('#{} {}'.format(test_case, result))
