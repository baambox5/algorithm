import sys
sys.stdin = open('5110.txt', 'r')


class LinkedList:
    def __init__(self, data, prev, next=None):
        self.data = data
        self.prev = prev
        self.next = next
        if prev:
            prev.next = self


for test_case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    head = None
    for k in range(M):
        arr = list(map(int, input().split()))
        if k:
            link = head
            for i in range(k * N):
                if link.data > arr[0]:
                    for j in range(N):
                        link.prev = LinkedList(arr[j], link.prev, link)
                        if not i and not j:
                            head = link.prev
                    break
                link = link.next
            else:
                for j in range(N):
                    end = LinkedList(arr[j], end)
        else:
            for i in range(N):
                if i:
                    end = LinkedList(arr[i], end)
                else:
                    head = LinkedList(arr[0], head)
                    end = head
    print('#{}'.format(test_case), end=' ')
    for _ in range(10):
        print('{}'.format(end.data), end=' ')
        end = end.prev
    print()
