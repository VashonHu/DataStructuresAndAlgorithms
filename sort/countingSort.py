def counting_sort(alist, max_value=300):
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


if __name__ == "__main__":
    pass
