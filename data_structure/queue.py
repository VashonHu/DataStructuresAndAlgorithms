class Queue(object):
    def __init__(self, size=100):
        self.__head = self.__tail = 0
        self.__queue = []
        self.__size = size
        for x in range(self.__size):
            self.__queue.append(0)

    def enqueue(self, val):
        if self.full():
            print("this Queue is full !")
            return -1
        else:
            self.__queue[self.__tail] = val
            self.__tail = self.__nextindex(self.__tail)

    def dequeue(self):
        if self.empty():
            print("this Queue is empty!")
            return -1
        else:
            x = self.__queue[self.__head]
            self.__head = self.__nextindex(self.__head)
            return x

    def __nextindex(self, x):
        if x == self.__size - 1:
            x = 0
        else:
            x += 1
        return x

    def empty(self):
        return self.__head == self.__tail

    def full(self):
        return self.__head == self.__nextindex(self.__tail)
