class ListNode(object):
    def __init__(self, data, next=None):
        self.__data = data
        self.__next = next

    @property
    def next(self):
        return self.__next

    @property
    def data(self):
        return self.__data

    @next.setter
    def next(self, next):
        self.__next = next


"""
the head node is the first element with value in the linked list,rather then a null node
"""


class LinkedList(object):
    def __init__(self):
        self.__head = ListNode(None)
        self.__tail = ListNode(None)

    @property
    def head(self):
        return self.__head

    @property
    def tail(self):
        return self.__tail

    def purge(self):
        self.__head = None
        self.__tail = None

    def is_empty(self):
        return self.__head.next is None

    def append(self, value):
        item = ListNode(value, None)

        if self.is_empty():
            self.__head.next = item
        else:
            self.__tail.next = item

        self.__tail = item

    def traverse(self):
        if self.is_empty():
            print("the LinkedList is empty!")
        else:
            p = self.head.next
            while p:
                print(p.data)
                p = p.next

    def remove(self, value):
        pointer = self.__head.next
        prepointer = self.__head

        while pointer and pointer.data != value:
            prepointer = pointer
            pointer = pointer.next

        if pointer is None:
            print("the value is in the Linked List!")
            return -1

        prepointer.next = pointer.next

        if pointer is self.__tail:
            self.__tail = prepointer
