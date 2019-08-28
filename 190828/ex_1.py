def enQueue(item):
    global rear
    if isFull():
        print('Queue_Full')
    else:
        rear += rear
        Q.append(item)


def deQueue():
    global front
    if isEmpty():
        Queue_Empty()
    else:
        front += 1
        Q.pop(front)


def isEmpty():
    return front == rear


def isFull():
    return (rear+1) % len(Q) == front


def Qpeek():
    if isEmpty():
        print('Queue_Empty')
    else:
        Q.pop(front+1)
Q = []
rear = -1
front = -1


# ------------------------------------------
import queue
q = queue.Queue()
q.put('A')

while not q.empty():
    print(q.get())
