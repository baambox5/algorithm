import sys
sys.stdin = open('2309.txt', 'r')


def perm(k, s, visit):
    if k == 7:        
        if s == 100:
            return order
        return
    elif s > 100:
        return
    else:
        for i in range(9):
            if visit & (1 << i): continue
            order[k] = i
            a = perm(k+1, s+arr[i], visit | (1 << i))
            if a != None:
                return a

arr = []
for _ in range(9):
    temp = int(input())
    if arr:
        for i in range(len(arr)):
            if arr[i] > temp:
                arr[i], temp = temp, arr[i]
        else:
            arr.append(temp)
    else:
        arr.append(temp)
order = [0] * 9
res = perm(0, 0, 0)
for i in range(7):
    print(arr[res[i]])
