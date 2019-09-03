import sys
sys.stdin = open('5120.txt', 'r')


class LinkedList:
    def __init__(self, data, prev, next=None):
        self.data = data
        self.prev = prev
        self.next = next
        if prev:
            prev.next = self


for test_case in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    head = None
    for i in range(N):
        if i:
            end = LinkedList(arr[i], end)
        else:
            head = LinkedList(arr[0], head)
            end = head
    end.next = head
    head.prev = end
    link = head
    for _ in range(K):
        for _ in range(M):
            link = link.next
        if link == head:
            end = LinkedList(link.prev.data+link.data, link.prev, link)
            head.prev = end
        else:
            link.prev = LinkedList(link.prev.data+link.data, link.prev, link)
        link = link.prev
        N += 1
    print('#{}'.format(test_case), end=' ')
    for i in range(N):
        print(end.data, end=' ')
        if i == 9:
            break
        end = end.prev
    print()
