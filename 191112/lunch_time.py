import sys
sys.stdin = open('lunch_time.txt', 'r')
from collections import deque
import copy


def lunch(count, visit, s):
    if count == person:
        q1 = copy.deepcopy(Q1)
        q2 = copy.deepcopy(Q2)
        time_check(q1, q2)
        return
    else:
        for i in range(s, person):
            if visit & (1 << i):
                continue
            Q1.append((time1[i], stair[0][2], 0, 0))
            lunch(count + 1, visit | (1 << i), i + 1)
            Q1.pop()
            Q2.append((time2[i], stair[1][2], 0, 0))
            lunch(count + 1, visit | (1 << i), i + 1)
            Q2.pop()


def time_check(q1, q2):
    global min_time
    count = 0
    result1 = 0
    result2 = 0
    while q1:
        time, stair_time, result1, check = q1.popleft()
        if time:
            q1.append((time - 1, stair_time, result1 + 1, 0))
        else:
            if stair_time:
                if count < 3:
                    q1.append((0, stair_time - 1, result1 + 1, 1))
                    count += 1
                else:
                    if check:
                        q1.append((0, stair_time - 1, result1 + 1, 1))
                    else:
                        q1.append((0, stair_time, result1 + 1, 0))
            else:
                count -= 1
    count = 0
    while q2:
        time, stair_time, result2, check = q2.popleft()
        if time:
            q2.append((time - 1, stair_time, result2 + 1, 0))
        else:
            if stair_time:
                if count < 3:
                    q2.append((0, stair_time - 1, result2 + 1, 1))
                    count += 1
                else:
                    if check:
                        q2.append((0, stair_time - 1, result2 + 1, 1))
                    else:
                        q2.append((0, stair_time, result2 + 1, 0))
            else:
                count -= 1

    if max(result1, result2) < min_time:
        min_time = max(result1, result2)


for test_case in range(1, int(input()) + 1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    people = []
    stair = []
    min_time = 40
    person = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                people += [(i, j)]
                person += 1
            elif arr[i][j] > 1:
                stair += [(i, j, arr[i][j])]
    time1 = []
    time2 = []
    for i in range(person):
        time1 += [abs(stair[0][0]-people[i][0]) + abs(stair[0][1]-people[i][1])]
        time2 += [abs(stair[1][0]-people[i][0]) + abs(stair[1][1]-people[i][1])]
    Q1 = deque()
    Q2 = deque()
    lunch(0, 0, 0)
    print('#{} {}'.format(test_case, min_time))
