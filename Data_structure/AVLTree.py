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

