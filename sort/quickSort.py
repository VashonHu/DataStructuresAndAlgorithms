from auxiliary_tool.swap_list import swap_list
from auxiliary_tool.random_list import random_list

'''
快排的原理是每次抽出一个数, 每次排序完之后, 这个数的左边全是大于等于它的数, 它的右边都是小于它的数
'''


def quick_sort(alist):
    return quick_sort_split(alist, 0, len(alist) - 1)


def quick_sort_split(alist, start, end):
    if start < end:
        mid = quick_sort_real(alist, start, end)
        quick_sort_split(alist, start, mid - 1)
        quick_sort_split(alist, mid + 1, end)


def quick_sort_real(alist, start, end):
    i = start - 1
    key = alist[end]

    for x in range(start, end + 1):
        if alist[x] < key:  # 在这里, i 其实指向的是key的分界线, 小于key的, 在i的左边, 大于key的, 在i的右边
            i += 1  # 因为i一直指向最后一个小于key的位置, 所以当这里的if成立时, 就将那个数移动到最后一个小于key的位置
            swap_list(alist, x, i)
    swap_list(alist, i + 1, end)
    return i + 1  # 这里不能忘记是+1


if __name__ == '__main__':
    the_list = random_list()
    quick_sort(the_list)
    print(the_list)
