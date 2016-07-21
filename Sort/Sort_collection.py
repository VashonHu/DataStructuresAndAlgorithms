import random
import sys

def insert_sort(alist):
    #go backward
    for i in range(1, len(alist)):
        key = alist[i]
        j = i - 1
        while j >= 0 and alist[j] > key:
            alist[j + 1] = alist[j]
            j -= 1
        alist[j + 1] = key

    return alist

def shell_sort(alist):
    #from back to go forward
    increment = len(alist) / 2
    while increment > 0:
        for j in range(increment, len(alist)):
            key = alist[j]
            k = j - increment
            while k >= 0 and alist[k] > key:
                alist[k + increment] = alist[k]
                k -= increment
            alist[k + increment] = key
        increment /= 2

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
            list_swap(alist, x, i)
    list_swap(alist, i + 1, end)
    return i + 1

def counting_sort(alist, max_value = 300):
    c = []
    for x in range(max_value):
        c.append(0)

    for x in alist:
        c[x] += 1

    for x in range(1, len(c)):
        c[x] += c[x - 1]

    b = alist[:]
    for x in range(len(alist) - 1, -1, -1):
        b[c[alist[x]] - 1] = alist[x]

    return b

def swap_list(alist, a, b):
    alist[a], alist[b] = alist[b], alist[a]

def random_list(max_size = 10, min_value = 30):
    import random
    import sys

    alist = []
    n = random.randrange(min_value)
    for x in range(max_size):
        n += random.randrange(3, 33, 3)
        alist.append(n)

    for x in range(max_size - 1):
        swap_list(alist, x, random.randint(x + 1, max_size - 1))

    return alist


def list_swap(alist, a, b):
    alist[a], alist[b] = alist[b], alist[a]

def bucket_sort(alist):
    b = []
    for x in range(10):
        b.append([])

    for x in alist:
        c = x * 10
        b[int(x)  ].append(x)

    for x in range(10):
        insert_sort(b[x])

    x = 0
    for i in range(10):
        for j in range(len(b[i])):
            alist[x] = b[i][j]
            x += 1

if __name__ == "__main__":
    alist = []
    for x in range(10):
        alist.append(random.random())

    print 'before:  ' , alist
    bucket_sort(alist)
    print 'after: ' , alist










