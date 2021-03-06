from auxiliary_tool.random_list import random_list


def shell_sort(alist):
    # from back to go forward
    increment = len(alist) // 2
    while increment > 0:
        for j in range(increment, len(alist)):
            key = alist[j]
            k = j - increment
            while k >= 0 and alist[k] > key:
                alist[k + increment] = alist[k]
                k -= increment
            alist[k + increment] = key
        increment //= 2
    return alist


if __name__ == '__main__':
    print(shell_sort(random_list()))