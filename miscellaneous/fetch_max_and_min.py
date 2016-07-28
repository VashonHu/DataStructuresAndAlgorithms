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

def swap_list(alist, a, b):
    alist[a], alist[b] = alist[b], alist[a]

def min_and_max(alist):
    max_n = min_n = this_max = this_min = alist[0]

    if len(alist) % 2 == 0:
        max_n = max(alist[0], alist[1])
        min_n = min(alist[0], alist[1])

    i = 1
    j = 2
    while j < len(alist):
        this_max = max(alist[i], alist[j])
        this_min = min(alist[i], alist[j])

        if this_max > max_n:
            max_n = this_max

        if this_min < min_n:
            min_n = this_min

        i += 1
        j += 1

    return max_n, min_n

if __name__ == "__main__":
    alist = random_list(9)
    print alist
    print min_and_max(alist)