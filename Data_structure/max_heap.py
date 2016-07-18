import sys
import random

class max_heap(object):
    def __init__(self):
        self.data = []
        self.size = 0

    def length(self):
        return len(self.data)

    def left(self, index):
        return index * 2

    def right(self, index):
        return index * 2 + 1

    def parent(self, index):
        return index / 2

    def max_heapiey(self, i):
        l = self.left(i)
        r = self.right(i)

        largest = 0
        if l < self.size and self.data[l] > self.data[i]:
            largest = l
        else:
            largest = i

        if r < self.size and self.data[r] > self.data[largest]:
            largest = r

        if largest != i:
            self.swap(i, largest)
            self.max_heapiey(largest)

    def swap(self, a, b):
        self.data[a], self.data[b] = self.data[b], self.data[a]

    def build(self):
        self.size = self.length()
        for x in range(self.size / 2, -1, -1):
            self.max_heapiey(x)

    def increase(self,i, key):
        if self.data[i] >= key:
            print "error, key value is too small!"
            return -1
        self.data[i] = key
        self.max_heapiey(i)
        while i >= 0 and self.data[self.parent(i)] < self.data[i]:
            self.swap(self.parent(i), i)
            i = self.parent(i)

    def insert(self, key):
        self.size += 1
        self.data.append(-sys.maxsize)
        self.increase(self.size - 1, key)

    def auto_make(self, size = 10):
        for x in range(size):
            self.insert(random.randrange(100))
        return self.data

    def heapsort(self):
        backup = self.data[:]
        for i in range(self.length() - 1, -1, -1):
            self.swap(0, i)
            self.size -= 1
            self.max_heapiey(0)
        result = self.data[:]
        self.data = backup
        self.size = len(backup)
        return result

    def extract(self):
        if self.size < 1:
            print "the heap is underflow!"
            return 0
        max = self.data[0]
        self.data[0] = self.data[self.size - 1]
        self.size -= 1
        self.max_heapiey(0)
        return max

    def show_heap(self):
        for x in range(self.size):
            print self.data[x],
        print

if __name__ == "__main__":
    a = max_heap()
    a.auto_make()
    a.show_heap()
    a.extract()
    a.show_heap()
