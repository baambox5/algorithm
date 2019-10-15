import sys
sys.stdin = open('5249.txt', 'r')


def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]


for test_case in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    Edge = []
    for _ in range(E):
        Edge.append(tuple(map(int, input().split())))
    Edge.sort(key=lambda x: x[2])
    p = [x for x in range(V + 1)]
    weight = 0
    cnt = 0
    cur = 0
    while cnt < V:
        u, v, w = Edge[cur]
        a = find_set(u); b = find_set(v)
        if a != b:
            p[b] = a
            weight += w
            cnt += 1
        cur += 1
    print('#{} {}'.format(test_case, weight))
