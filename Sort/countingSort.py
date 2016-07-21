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
        b[c[alist[x]] - 1]
，		= alist[x]

    return b

def swap_list(alist, a, b):
    alist[a], alist[b] = alist[b], alist[a]

def random_list(max_size = 10, min_value = 30, ):
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

if __name__ == "__main__":
    print counting_sort( random_list(10, 100))