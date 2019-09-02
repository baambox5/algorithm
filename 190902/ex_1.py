class Node:
    def __init__(self, data, link):
        self.data = data
        self.link = link

    def addtoFirst(data):   # 첫 노드에 데이터 삽입
        global Head
        Head = Node(data, Head)

    def addtoLast(data):    # 마지막에 데이터 삽입
        global Head
        if Head == None:    # 빈 리스트이면
            Head = Node(data, None)
        else:
            p = Head
            while p.link != None:   # 마지막 노드를 찾을때까지
                p = p.link
            p.link = Node(data, None)

    def delete(pre):    # pre 다음 노드 삭제
        if pre == None or pre.link == None:
            print('error')
        else:
            pre.link = pre.link.link


data = [1, 2, 3, 4]
Head = None

for i in range(len(data)):
    Node.addtoFirst(data[i])

while Head.link != None:
    print(Head.data, end='->')
    Head = Head.link
print(Head.data)