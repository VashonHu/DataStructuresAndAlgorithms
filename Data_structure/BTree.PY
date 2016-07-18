class BTreeNode(object):
    def __init__(self, leaf = True):
        self.keys = []
        self.children = []
        self.leaf = True
        
class BTree(object):
    def __init__(self, t = 4):
        self.t = t
        self.root = self.new_node()
    
    def search(self, x, k):
        i = 0
        while i < len(x) and k > x.keys[i]:
            i += 1
        if i < len(x) and k == x.keys[i]:
            return (x, i)
        elif x.leaf:
            return None
        else:
            return self.search(x.children[i], k)
    #
    # def create(self):
    #     self.root = self.new_node()
    
    def new_node(self, leaf = True):
        node = BTreeNode(leaf)
        for x in range(2 * self.t - 1):
            node.keys.append(None)
        for x in range(2 * self.t):
            node.children.append(None)
        return node
        
    def split_child(self, x, i):
        z = self.new_node()
        y = x.children[i]
        z.leaf = y.leaf

        for j in range(1, self.t):
            z.keys[j] = y.keys[j + self.t]
        for j in range(1, self.t + 1):
            z.children[j] = y.keys[j + self.t]

        for j in range(len(x.children), i - 1, -1):
            x.children[j + 1] = x.children[j]
        x.children[j + 1] = z

        for j in range(len(x.keys), i - 1, -1):
            x.keys[j + 1] = x.keys[j]
        x.children[j] = y.keys[self.t]

    def insert(self, k):
        r = self.root
        if len(r.keys) == self.t * 2 - 1:
            s = self.new_node(False)
            self.root = s
            s.children[0] = r
            self.split_child(s, 0)
            self.insert_no_full(s, k)
        else:
            self.insert_no_full(r, k)

    def insert_no_full(self, x, k):
        i = len(x.keys) - 1
        if x.leaf:
            while i >= 0 and k < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
        else:
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1
            if x.children[i] == self.t * 2 - 1:
                self.split_child(x, i)
                if k > x.keys[i]:
                    i += 1
            self.insert_no_full(x.children[i], k)


if __name__ == "__main__":
    a = BTree()
    for i in range(10):
        a.insert(i)



        
        
        