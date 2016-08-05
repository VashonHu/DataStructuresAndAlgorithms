from auxiliary_tool.swap_list import swap_list

def quick_sort(alist):
    return quick_sort_split(alist, 0, len(alist) - 1)

def quick_sort_split(alist, start, end):
    if start < end:
        mid = quick_sort_real(alist, start, end)
        quick_sort_split(alist, start, mid - 1)
        quick_sort_split(alist, mid +  1, end)

def quick_sort_real(alist, start, end):
    i = start - 1
    key = alist[end]

    for x in range(start, end + 1):
        if alist[x] < key:
            i += 1
            swap_list(alist, x, i)
    swap_list(alist, i + 1, end)
    return i + 1
