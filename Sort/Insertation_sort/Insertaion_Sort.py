import random

def insert_sort(alist):
    for i in range(1, len(alist)):
        key = alist[i]
        j = i -1
        while j >= 0 and alist[j] > key:
            alist[j + 1] = alist[j]
            j -= 1
        alist[j + 1] = key

    return alist

def random_list(max_size = 100, min_value = 0, max_value = 5, repeat = 0):
    alist = []
    if repeat == 1:
        notrepeat = 0
    else:
        notrepeat = 1

    for i in range(max_size ):
        if(min_value + repeat < max_value):
            alist.append(random.randint(min_value + notrepeat, max_value))
            notrepeat += 1
        else:
            print "random's range is wrong!\n"
    return alist

if __name__ == "__main__":
    alist = random_list( max_size = 5,repeat =  True)
    print 'before:  ' , alist
    insert_sort(alist)
    print 'after: ' , alist










