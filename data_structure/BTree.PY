class BTreeNode(object):
    def __init__(self, leaf=True):
        self.keys = []
        self.children = []
        self.leaf = leaf
        self.n = 0


class BTree(object):
    def __init__(self, t=4):
        self.t = t
        self.root = self.new_node()

    def search(self, x, k):
        i = 0
        while i < x.n and k > x.keys[i]:
            i += 1
        if i < x.n and k == x.keys[i]:
            return (x, i)
        elif x.leaf:
            return None
        else:
            return self.search(x.children[i], k)

    def new_node(self, leaf=True):
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

        for m, n in enumerate(range(self.t, self.t * 2 - 1)):
            z.keys[m] = y.keys[n]
        if not y.leaf:
            for m, n in enumerate(range(self.t, 2 * self.t)):
                z.children[m] = y.children[n]
        z.n = self.t - 1
        y.n = self.t - 1

        for n in range(x.n, i, -1):
            x.children[n + 1] = x.children[n]
        x.children[i + 1] = z

        for n in range(x.n - 1, i - 1, -1):
            x.keys[n + 1] = x.keys[n]
        x.keys[i] = y.keys[self.t - 1]
        x.n += 1

    def insert(self, k):
        r = self.root
        if r.n == self.t * 2 - 1:
            s = self.new_node(False)
            self.root = s
            s.children[0] = r
            self.split_child(s, 0)
            self.insert_no_full(s, k)
        else:
            self.insert_no_full(r, k)

    def insert_no_full(self, x, k):
        i = x.n - 1
        if x.leaf:
            while i >= 0 and k < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
            x.n += 1
        else:
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1
            if x.children[i].n == self.t * 2 - 1:
                self.split_child(x, i)
                if k > x.keys[i]:
                    i += 1
            self.insert_no_full(x.children[i], k)

    def traverse(self):
        def traverse_real(self, t):
            if t is not None:
                for x in range(self.t * 2):
                    traverse_real(self, t.children[x])
                for x in range(t.n):
                    if x is not None:
                        print(t.keys[x], end='')
                print("")

        traverse_real(self, self.root)


if __name__ == "__main__":
    a = BTree()
    for i in range(10):
        a.insert(i)

    i = 50
    a.insert(50)

    # i = 51
    # a.insert(51)
    print(a.traverse(), end='')
