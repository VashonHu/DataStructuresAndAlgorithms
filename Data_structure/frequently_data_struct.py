class stack(object):
    def __init__(self):
        self.__stack = []

    def push(self, val):
        self.__stack.append(val)

    def __empty(self):
        return len(self.__stack) == 0

    def pop(self):
        if self.__empty():
           print "this stack is underflow"
           return -1

        element =  self.__stack[-1]
        del self.__stack[-1]
        return element

class queue(object):
    def __init__(self, size = 100):
        self.__head = self.__tail = 0
        self.__queue = []
        self.__size = size
        for x in range(self.__size):
            self.__queue.append(0)

    def enqueue(self, val):
        if self.__full():
            print "this queue is full !"
            return -1
        else:
            self.__queue[self.__tail] = val
            self.__tail = self.__nextindex(self.__tail)

    def dequeue(self):
        if self.__empty():
            print "this queue is empty!"
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

    def __empty(self):
        return self.__head == self.__tail

    def __full(self):
        return self.__head == self.__nextindex(self.__tail)

class ListNode(object):
    def __init__(self, data, next = None):
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
            print "the LinkedList is empty!"
        else:
            p = self.head.next
            while p :
                print p.data
                p = p.next

    def remove(self, value):
        pointer = self.__head.next
        prepointer = self.__head

        while pointer and pointer.data != value:
            prepointer = pointer
            pointer = pointer.next

        if pointer is None:
            print "the value is in the Linked List!"
            return -1

        prepointer.next = pointer.next

        if pointer is self.__tail:
            self.__tail = prepointer


class AVLTreeNode(object):
    def __init__(self, data, left = None, right = None, height = -1):
        self.data = data
        self.left = left
        self.right = right
        self.height = height


class AVLTree(object):
    def __init__(self):
        self.__tree = None

    def height(self, tree):
        if tree is None:
            return -1
        else:
            return tree.height

    def append(self, x):
        def apppend_aide(self, x, tree):
            if tree is None:
                tree = AVLTreeNode(x)
            elif x < tree.data:
                tree.left = apppend_aide(self, x, tree.left)
                if self.height(tree.left) - self.height(tree.right) is  2:
                    if x < tree.left.data:
                        tree = self.singleRotateWithLeft(tree)
                    else:
                        tree = self.doubleRotateWithLeft(tree)
            elif x > tree.data:
                tree.right = apppend_aide(self, x, tree.right)
                if self.height(tree.right) - self.height(tree.left) is 2:
                    if x > tree.right.data:
                        tree = self.singleRotateWithRight(tree)
                    else:
                        tree = self.doubleRotateWithRihgt(tree)
            tree.height = max(self.height(tree.left), self.height(tree.right)) + 1
            return tree

        self.__tree = apppend_aide(self, x, self.__tree)

    def delete(self, item):
        def delete_aide(self, tree, item):
            if tree is None:
                print "The item is not found!"
            elif item < tree.data:
                tree.left = delete_aide(self, tree.left, item)
            elif item > tree.data:
                tree.right = delete_aide(self, tree.right, item)
            elif tree.left and tree.right:
                tree.data = self.find_min(tree.right).data
                tree.right = delete_aide(self, tree.right, tree.data)
            else:
                if tree.left is None:
                    tree = tree.left
                elif tree.right is None:
                    tree = tree.right

            return tree

        self.__tree = delete_aide(self, self.__tree, item)

    # def find_min(self, tree):
    #     p = tree[:]
    #     while p and p.left is not None:
    #         p = p.left
    #
    #     return p
    def find_min(self, tree):
        if tree and tree.left:
            self.find_min(tree.left)
        else:
            return tree

    def traverse(self):
        print "the tree is :",
        def traverse_aide(self, tree):
            if tree is not None:
                traverse_aide(self, tree.left)
                traverse_aide(self, tree.right)
                print tree.data,
        traverse_aide(self, self.__tree)
        print

    def singleRotateWithLeft(self, node_a):
        node_b = node_a.left

        node_a.left = node_b.right
        node_b.right = node_a

        node_a.height = max(self.height(node_a.right), self.height(node_a.left)) + 1
        node_b.height = max(self.height(node_a.left), self.height(node_a)) + 1

        return node_b

    def doubleRotateWithRihgt(self, node_a):
        node_a.left = self.singleRotateWithRight(node_a.right)
        return self.doubleRotateWithLeft(node_a)

    def singleRotateWithRight(self, node_a):
        node_b = node_a.right

        node_a.right = node_b.left
        node_b.left = node_a

        node_a.height = max(self.height(node_a.right), self.height(node_a.left)) + 1
        node_b.height = max(self.height(node_b.right), self.height(node_a)) + 1

        return node_b

    def doubleRotateWithLeft(self, node_a):
        node_a.right = self.singleRotateWithLeft(node_a.right)
        return self.singleRotateWithRight(node_a)

class RBTNode(object):
    def __init__(self, data, left = None, right = None, color = True, height = -1):
        self.data = data
        self.left = left
        self.right = right
        self.color = color
        self.height = height

class RBTree(object):
    def __init__(self):
        self.tree = None
        self.red = True
        self.black = False

    def isRed(self, node):
        if node is None:
             return False
        return node.color

    def chageColor(self, node):
        node.color = self.red
        node.left.color = node.right.color = self.black
        return node

    def rotateLeft(self, a):
        b = a.right

        a.right = b.left
        b.left = a

        b.color = a.color
        a.color = self.red

        a.height = max(self.height(a.right), self.height(a.left)) + 1
        b.height = max(self.height(a), self.height(b.right)) + 1

        return b

    def rotateRight(self, a):
        b = a.left

        a.left = b.right
        b.right = a
        b.color = a.color
        a.color = self.red

        a.height = max(self.height(a.right), self.height(a.left)) + 1
        b.height = max(self.height(a), self.height(b.left)) + 1
        return b

    def append(self, val):
        def append_real(self, h, val):
            if h is None:
                h = RBTNode(val)
            elif val < h.data:
                h.left = append_real(self, h.left, val)
            elif val > h.data:
                h.right = append_real(self, h.right, val)

            if self.isRed(h.right) and not self.isRed(h.left):
                h = self.rotateLeft(h)
            if self.isRed(h.left) and self.isRed(h.left.left):
                h = self.rotateRight(h)
            if self.isRed(h.left) and self.isRed(h.right):
                h = self.chageColor(h)

            h.height = max(self.height(h.right), self.height(h.left)) + 1
            return h

        self.tree = append_real(self, self.tree, val)
        self.tree.color = self.black

    def height(self, node):
        if node is None:
            return -1
        return node.height

    def traverse(self):
        print "the tree is :",
        def traverse_aide(self, tree):
            if tree is not None:
                traverse_aide(self, tree.left)
                traverse_aide(self, tree.right)
                print tree.data,

        traverse_aide(self, self.tree)
        print

if __name__ == "__main__":
    a = RBTree()

    for x in range(11):
        a.append(x)

    a.traverse()

    b = AVLTree()

    for x in range(11):
        b.append(x)

    b.traverse()

