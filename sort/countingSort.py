from auxiliary_tool.random_list import random_list


def counting_sort(alist, max_value=300):
    c = []
    for x in range(max_value):
        c.append(0)

    for x in alist:
        c[x] += 1

    for x in range(1, len(c)):
        c[x] += c[x - 1]  # c[x]的数值表示该数组中, 有多少个数小于或等于x, 也就是它在数组中的位置

    b = alist[:]
    for x in range(len(alist) - 1, -1, -1):
        b[c[alist[x]] - 1] = alist[x]  # 减-的原因在于c的数组中对应的值只是它在数组中的位置, 而要得出下标, 必须将其减一
        c[alist[x]] -= 1

    return b


if __name__ == "__main__":
    print(counting_sort([3, 5, 1, 2, 5, 8, 4, 2]))
