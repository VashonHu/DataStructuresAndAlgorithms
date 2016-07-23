class RBTNode(object):
    def __init__(self, data, left = None, right = None, color = True, parent = None, size = 0):
        self.data = data
        self.left = left
        self.right = right
        self.color = color
        self.parent = parent
        self.size = size

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

        b.parent = a.parent
        a.parent = b

        b.color = a.color
        a.color = self.red

        b.size = a.size
        a.size = self.size(a.right) + self.size(a.left) + 1

        return b

    def rotateRight(self, a):
        b = a.left

        a.left = b.right
        b.right = a

        b.parent = a.parent
        a.parent = b

        b.color = a.color
        a.color = self.red

        b.size = a.size
        a.size = self.size(a.right) + self.size(a.left) + 1
        return b

    def append(self, val):
        def append_real(self, h, val):
            if h is None:
                h = RBTNode(val)
            elif val < h.data:
                h.left = append_real(self, h.left, val)
                h.left.parent = h
            elif val > h.data:
                h.right = append_real(self, h.right, val)
                h.right.parent = h

            if self.isRed(h.right) and not self.isRed(h.left):
                h = self.rotateLeft(h)
            if self.isRed(h.left) and self.isRed(h.left.left):
                h = self.rotateRight(h)
            if self.isRed(h.left) and self.isRed(h.right):
                h = self.chageColor(h)

            h.size = self.size(h.right) + self.size(h.left) + 1
            return h

        self.tree = append_real(self, self.tree, val)
        self.tree.color = self.black

    def size(self, node):
        if node is None:
            return 0
        return node.size

    def traverse(self):
        print "the tree is :",
        def traverse_aide(self, tree):
            if tree is not None:
                traverse_aide(self, tree.left)
                traverse_aide(self, tree.right)
                print tree.data,

        traverse_aide(self, self.tree)
        print

    def os_select(self, i):#find the order of the element is i
        def os_select_real(self, tree, i):
            r = tree.left.size + 1
            if i == r:
                return tree
            elif i < r:
                return os_select_real(self, tree.left, i)
            return os_select_real(self, tree.right, i - r)

        return os_select_real(self, self.tree, i)

    def rank(self, x):#return the order of x element in middle order traversal
        def rank_real(self, tree, x):
            r = tree.left.size + 1
            y = self.os_select(x)
            while y is not self.tree:
                if y is y.parent.right:
                    r = r + y.parent.left.size + 1
                y = y.parent
            return r

        return rank_real(self, self.tree, x)

if __name__ == "__main__":
    a = RBTree()
    for x in range(3):
        a.append(x)

    for x in range(3):
        pass
    print a.os_select(x).data