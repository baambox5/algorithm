def backtrack(a, k, input):
    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES
    if k == input:
        process_solution(a, k)  # 답이면 원하는 작업
    else:
        k += 1
        ncandidates = construct_candidates(a, k, input, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, input)


def construct_candidates(a, k, input, c):
    c[0] = True
    c[1] = False
    return 2


def process_solution(a, k):
    sum_value = 0
    for i in range(k + 1):
        if a[i]:
            sum_value += i
    if sum_value == 10:
        print('(', end=' ')
        for i in range(k + 1):
            if a[i]:
                print(i, end=' ')
        print(')')


MAXCANDIDATES = 100
NMAX = 100
a = [0] * NMAX
backtrack(a, 0, 10)
