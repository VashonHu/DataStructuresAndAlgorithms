import sys

from auxiliary_tool.random_list import random_list


def merge_sort(alist):
    split_merge(alist, 0, len(alist) - 1)


def split_merge(alist, start, end):
    if start < end:
        mid = (start + end) // 2
        split_merge(alist, start, mid)
        split_merge(alist, mid + 1, end)
        merge(alist, start, mid, end)


def merge(alist, start, mid, end):
    left_list = (alist[element] for element in range(start, mid + 1))
    right_list = (alist[element] for element in range(mid + 1, end + 1))

    left_list = (*left_list, sys.maxsize)
    right_list = (*right_list, sys.maxsize)

    i = 0
    j = 0
    for k in range(start, end + 1):  # 最小的时候, 两个数组分别只有一个数, 而每次比较以后, 两个数组都是有序的,
        if left_list[i] <= right_list[j]:
            alist[k] = left_list[i]
            i += 1
        else:
            alist[k] = right_list[j]
            j += 1


if __name__ == '__main__':
    a_list = random_list(10000)
    print(a_list)
    merge_sort(a_list)
    print(a_list)
