import sys

def merge_sort(alist):
    split_merge(alist, 0, len(alist) - 1)

def split_merge(alist, start, end):
    if start < end:
        mid = (start + end) / 2
        split_merge(alist, start, mid)
        split_merge(alist, mid + 1, end)
        merge(alist, start, mid, end)

def merge(alist, start, mid, end):
    left_list = []
    right_list = []

    for element in range(start, mid + 1):
        left_list.append(alist[element])
    for element in range(mid + 1, end + 1):
        right_list.append(alist[element])

    #set sentrys
    left_list.append(sys.maxsize)
    right_list.append(sys.maxsize)

    i = 0
    j = 0
    for k in range(start, end + 1):
        if left_list[i] <= right_list[j]:
            alist[k] = left_list[i]
            i += 1
        else:
            alist[k] = right_list[j]
            j += 1
