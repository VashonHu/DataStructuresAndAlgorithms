class RBTNode(object):
    def __init__(self, data, left=None, right=None, color=True, height=-1):
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
        node.color = self.red  # color等于True时, 表示红色; 等于False时, 表示黑色
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
            '''
            1. 每个节点或红或黑
            2. 每个叶子节点都是黑的
            3. 根节点是黑色
            4. 如果一个结点是红色的, 那么它的两个孩子都是黑色的
            5. 对于每个结点, 到每个叶节点的简单路径上, 黑结点的数目都是相同的
            
            
            1. 不存在连续的红链接
            2. 红链接都是左链接
            3. 
            '''
            if self.isRed(h.right) and not self.isRed(h.left):  # 如果左黑, 右红: 存在红色的右链接
                h = self.rotateLeft(h)
            if self.isRed(h.left) and self.isRed(h.left.left):  # 左红, 左左红, 右旋转:存在连续的红链接
                h = self.rotateRight(h)
            if self.isRed(h.left) and self.isRed(h.right):  # 左右都红, 转变颜色: 自己改为红色, 左右孩子都转为黑色
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
        print("the tree is :", end=' ')

        def traverse_aide(self, tree):
            if tree is not None:
                traverse_aide(self, tree.left)
                traverse_aide(self, tree.right)
                print(tree.data, end=' ')

        traverse_aide(self, self.tree)
        print(' ')


if __name__ == "__main__":
    a = RBTree()

    for x in range(11):
        a.append(x)

    a.traverse()
