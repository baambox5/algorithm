import sys
sys.stdin = open('5108.txt', 'r')


class LinkedList:
    def __init__(self, i, data, link):
        self.idx = i
        self.data = data
        self.link = link


for test_case in range(1, int(input()) + 1):
    N, M, L = map(int, input().split())
    head = None
    idx = 0
    for string in input().split():
        head = LinkedList(idx, string, head)
        idx += 1
    for _ in range(M):
        idx_in, number_in = map(int, input().split())
        link = head
        for i in range(head.idx+1):
            if link.idx > idx_in:
                link.idx += 1
            elif link.idx == idx_in:
                link.link = LinkedList(link.idx, number_in, link.link)
                link.idx += 1
                break
            link = link.link
    link = head
    for _ in range(head.idx+1):
        if link.idx == L:
            print('#{} {}'.format(test_case, link.data))
            break
        link = link.link
