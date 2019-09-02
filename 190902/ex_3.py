# 병합정렬
def merge_sort(a):
    if len(a) <= 1:
        return a
    else:
        mid = len(a) // 2
        left = a[:mid]
        right = a[mid:]

        left = merge_sort(left)
        right = merge_sort(right)

        return merge(left, right)


def merge(l, r):
    res = []
    while len(l) > 0 and len(r) > 0:
        if l[0] < r[0]:
            res.append(l.pop(0))
        else:
            res.append(r.pop(0))
    if len(l) > 0:
        res.extend(l)
    if len(r) > 0:
        res.extend(r)
    return res


arr = [69, 10, 30, 2, 16, 8, 31, 22]
print('정렬 전: {}'.format(arr))
arr_sort = merge_sort(arr)
print('정렬 후 : {}'.format(arr_sort))
