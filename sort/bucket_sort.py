import random
import sys

def insert_sort(alist):
    for i in range(1, len(alist)):
        key = alist[i]
        j = i -1
        while j >= 0 and alist[j] > key:
            alist[j + 1] = alist[j]
            j -= 1
        alist[j + 1] = key

    return alist


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










