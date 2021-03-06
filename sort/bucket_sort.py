import random


def insert_sort(alist):
    for i in range(1, len(alist)):
        key = alist[i]
        j = i - 1
        while j >= 0 and alist[j] > key:
            alist[j + 1] = alist[j]
            j -= 1
        alist[j + 1] = key

    return alist


def bucket_sort(alist):
    # 构建一个数组, 数组元素从0到9
    # 这里的桶排序只应用与小于1的数
    b = []
    for x in range(10):
        b.append([])

    for x in alist:
        c = x * 10  # x都是小于1的数
        b[int(x)].append(x)

    for x in range(10):
        insert_sort(b[x])

    x = 0
    for i in range(10):
        for j in range(len(b[i])):
            alist[x] = b[i][j]
            x += 1


if __name__ == "__main__":
    alist = []
    for x in range(100):
        alist.append(random.random())
    bucket_sort(alist)
    print(alist)
