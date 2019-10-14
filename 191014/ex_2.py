# MST


def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]


V, E = map(int, input().split())
# G = [[] for _ in range(V)]  # 0 ~ V - 1
Edge = []
for _ in range(E):
    # u, v, w = map(int, input().split())
    # G[u].append((v, w))
    # G[v].append((v, w))
    Edge.append(tuple(map(int, input().split())))

Edge.sort(key=lambda x: x[2])
p = [x for x in range(V)]
# V - 1개의 간선을 선택
MST = []
cur = 0
while len(MST) < V - 1:
    u, v, w = Edge[cur]
    a = find_set(u); b = find_set(v)
    if a != b:
        p[b] = a
        MST.append((u, v, w))
    cur += 1

