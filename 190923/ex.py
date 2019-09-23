arr = [69, 10, 30, 2, 16, 8, 31, 22]
tmp = [0] * len(arr)


# def merge_sort(lo, hi):
#     if lo == hi: return
#     # 분할
#     mid = (lo + hi) >> 1
#     merge_sort(lo, mid)  # 왼쪽
#     merge_sort(mid + 1, hi)  # 오른쪽
#     # 왼쪽과 오른쪽을 병합
#     i, j, k = lo, mid + 1, lo
#     while i <= mid and j <= hi:
#         if arr[i] < arr[j]:
#             tmp[k] = arr[i]
#             i, k = i + 1, k + 1
#         else:
#             tmp[k] = arr[j]
#             j, k = j + 1, k + 1
#     while i <= mid:
#         tmp[k] = arr[i]
#         i, k = i + 1, k + 1
#     while j <= hi:
#         tmp[k] = arr[j]
#         j, k = j + 1, k + 1
#     for i in range(lo, hi + 1):
#         arr[i] = tmp[i]
#
#
# print(arr)
# merge_sort(0, len(arr) - 1)
# print(arr)


# def quick_sort(lo, hi):
#     if lo >= hi: return
#     i, j, pivot = lo, hi, arr[lo]
#     while i < j:
#         while i <= hi and pivot >= arr[i]: i += 1
#         while pivot < arr[j]: j -= 1
#         if i < j:
#             arr[i], arr[j] = arr[j], arr[i]
#     arr[lo], arr[j] = arr[j], arr[lo]
#     quick_sort(lo, j - 1)
#     quick_sort(j + 1, hi)
#
#
# print(arr)
# quick_sort(0, len(arr) - 1)
# print(arr)


def quick_sort(lo, hi):
    if lo >= hi: return
    i = lo - 1
    for j in range(lo, hi):
        if arr[hi] >= arr[j]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    i += 1
    arr[hi], arr[i] = arr[i], arr[hi]
    quick_sort(lo, i - 1)
    quick_sort(i + 1, hi)


print(arr)
quick_sort(0, len(arr) - 1)
print(arr)
