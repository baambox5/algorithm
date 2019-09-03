import sys
sys.stdin = open('5122.txt', 'r')


class LinkedList:
    def __init__(self, i, data, prev):
        self.idx = i
        self.data = data
        self.prev = prev


for test_case in range(1, int(input()) + 1):
    N, M, L = map(int, input().split())
    arr = input().split()
    head = None
    str_in = ''
    for i in range(N):
        head = LinkedList(i, arr[i], head)
    for _ in range(M):
        str_in = input().split()
        char, idx_in = str_in[0], int(str_in[1])
        if len(str_in) == 3:
            number_in = str_in[2]
        link = head
        for _ in range(N):
            if char == 'I':
                if link.idx == idx_in:
                    link.prev = LinkedList(link.idx, number_in, link.prev)
                    link.idx += 1
                    N += 1
                    break
                elif idx_in > head.idx:
                    head = LinkedList(idx_in, number_in, head)
                    N += 1
                    break
                else:
                    link.idx += 1
            elif char == 'D':
                if head.idx == idx_in:
                    head = head.prev
                    N -= 1
                    break
                elif link.idx == idx_in + 1:
                    link.prev = link.prev.prev
                    link.idx -= 1
                    N -= 1
                    break
                else:
                    link.idx -= 1
            elif char == 'C':
                if link.idx == idx_in:
                    link.data = number_in
                    break
            link = link.prev
    for _ in range(N):
        if head.idx == L:
            print('#{} {}'.format(test_case, head.data))
            break
        head = head.prev
    else:
        print('#{} {}'.format(test_case, -1))
