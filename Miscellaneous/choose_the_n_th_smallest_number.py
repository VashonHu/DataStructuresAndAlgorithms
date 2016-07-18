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

def quick_sort(alist):
    return quick_sort_split(alist, 0, len(alist) - 1)


def quick_sort_split(alist, start, end):
    if end - start > 3:
        mid = quick_sort_real(alist, start, end)
        quick_sort_split(alist, start, mid - 1)
        quick_sort_split(alist, mid + 1, end)
    else:
        insert_sort(alist)

def quick_sort_real(alist, start, end):
    import random
    i = start - 1
    key = alist[end]

    for x in range(start, end + 1):
        if alist[x] < key:
            i += 1
            swap_list(alist, x, i)
    swap_list(alist, i + 1, end)
    return i + 1


def swap_list(alist, a, b):
    alist[a], alist[b] = alist[b], alist[a]


def random_list(max_size=10, min_value=30):
    import random
    import sys

    alist = []
    n = random.randrange(min_value)
    for x in range(max_size):
        n += random.randrange(3, 20)
        alist.append(n)

    for x in range(max_size - 1):
        swap_list(alist, x, random.randint(x + 1, max_size - 1))

    return alist

def select(alist, i):
    def select_real(p, r, i):
        if p == r:
            return alist[p]
        q = quick_sort_real(alist, p, r)
        if i == q:
            return alist[q]
        elif i < q:
            return select_real(p, q - 1, i)
        return select_real(q + 1, r, i - q)

    return select_real(0, len(alist) - 1, i - 1)

if __name__ == "__main__":
    alist = random_list()
    b = alist[:]
    quick_sort(b)
    print b
    print select(alist, 3)