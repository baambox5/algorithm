import sys
sys.stdin = open('gerrymandering.txt', 'r')


def select_dfs(x, visit):
    global sum_select
    sum_select += people[x]
    visit[x] = 1
    for y in graph[x]:
        if select_check[y] and not visit[y]:
            select_dfs(y, visit)


def dfs(x, visit):
    global sum_nselect
    sum_nselect += people[x]
    visit[x] = 1
    for y in graph[x]:
        if not visit[y]:
            dfs(y, visit)


def comb(k, s):
    global sum_select, sum_nselect, min_diff
    if k == i:
        sum_select, sum_nselect = 0, 0
        visit = [0] * (N + 1)
        select_dfs(select[0], visit)
        for n in range(i):
            if not visit[select[n]]:
                break
        else:
            check = 0
            for n in range(1, N + 1):
                if not visit[n]:
                    if check:
                        break
                    check = 1
                    dfs(n, visit)
            else:
                diff = abs(sum_nselect - sum_select)
                if min_diff > diff:
                    min_diff = diff
    else:
        for j in range(s, N + 1):
            select[k] = j
            select_check[j] = 1
            comb(k + 1, j + 1)
            select_check[j] = 0


N = int(input())
people = [0]
people += list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]
min_diff = 1000000
sum_select = 0
sum_nselect = 0
select_check = [0] * (N + 1)
for i in range(1, N + 1):
    close = list(map(int, input().split()))
    for j in range(1, close[0] + 1):
        graph[i] += [close[j]]
for i in range(1, N // 2 + 1):
    select = [0] * i
    comb(0, 1)
if min_diff == 1000000:
    min_diff = -1
print(min_diff)
