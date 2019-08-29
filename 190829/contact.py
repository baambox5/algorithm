import sys
sys.stdin = open('contact.txt', 'r')
from collections import deque

for test_case in range(1, 11):
    number, start = map(int, input().split())
    str_in = input().split()
    group = [[] for _ in range(number + 1)]
    visit = [0] * (number + 1)
    dist = [0] * (number + 1)
    for i in range(number // 2):
        group[int(str_in[2*i])].append(int(str_in[2*i+1]))
    q = deque()
    q.append(start)
    visit[start] = 1
    dist[start] = 1
    while q:
        s = q.popleft()
        for w in group[s]:
            if not visit[w]:
                visit[w] = 1
                dist[w] = dist[s] + 1
                q.append(w)
    max_value = 1
    for i in range(1, number + 1):
        if dist[i] >= max_value:
            max_value = dist[i]
            idx = i
    print('#{} {}'.format(test_case, idx))
