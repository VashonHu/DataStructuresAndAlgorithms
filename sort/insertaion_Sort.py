from auxiliary_tool.random_list import random_list


def insert_sort(alist):
    for i in range(1, len(alist)):
        key = alist[i]
        j = i - 1
        while j >= 0 and alist[j] > key:
            alist[j + 1] = alist[j]
            j -= 1
        alist[j + 1] = key

    return alist


if __name__ == "__main__":
    print(insert_sort(random_list()))
