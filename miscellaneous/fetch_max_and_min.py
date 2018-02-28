from auxiliary_tool.random_list import random_list


def min_and_max(alist):
    max_n = min_n = alist[0]

    if len(alist) % 2 == 0:  # 因为元素个数可能小于2的情况, 所以加上这个判断
        max_n = max(alist[0], alist[1])
        min_n = min(alist[0], alist[1])

    i = 1
    j = 2  # 数组个数小于3时, 这个循环不会运行
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
    alist = random_list(10)
    print(alist)
    print(min_and_max(alist))
