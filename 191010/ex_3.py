def preorder(n):
    if n:
        print(n, end=' ')
        preorder(arr[n][0])
        preorder(arr[n][1])


def inorder(n):
    if n:
        inorder(arr[n][0])
        print(n, end=' ')
        inorder(arr[n][1])


def postorder(n):
    if n:
        postorder(arr[n][0])
        postorder(arr[n][1])
        print(n, end=' ')


N = 13
in_str = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'
get_str = list(map(int, in_str.split()))
arr = [[0] * 2 for i in range(N + 1)]
for i in range(N - 1):
    if not arr[get_str[i*2]][0]:
        arr[get_str[i*2]][0] = get_str[i*2+1]
    else:
        arr[get_str[i*2]][1] = get_str[i*2+1]

print('전위 순회 결과 :', end=' ')
preorder(1)
print()

print('중위 순회 결과 :', end=' ')
inorder(1)
print()

print('후위 순회 결과 :', end=' ')
postorder(1)
print()
