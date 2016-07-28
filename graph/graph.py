from data_structure.hashTable import HashTable
import sys

GRAY = 1
BLACK = 2
WHITE = 3

class GraphNode(object):
    def __init__(self, key, color = WHITE,d = -sys.maxsize, p = None):
        self.key = key
        self.color = color
        self.d = d
        self.p = p
        self.adj = []
class Graph(object):
    def __init__(self):
        self.table = HashTable()
        self.tabelSize = self.table.tabelSize

    def findNode(self, k):
        hashVal = self.table.betterHash(k)
        return self.table.find(hashVal, k)

    def addNode(self, item):
        return self.table.insertion(item)

    def deleteNode(self, item):
        return self.table.delete(item)

    def findEdge(self,n, e):
        offset = 0
        if n == None or n.adj == []:
            return -1
        for x in n.adj:
            if x.key == e.key:
                return offset
            offset += 1
        return -1


    def addEdge(self, n, e):
        nodeIndex = self.findNode(n.key)
        try:
            if nodeIndex < 0:
                raise ValueError, "The node is not in the graph !"
        except ValueError, e:
            print e
            return

        self.addNode(e)

        node = self.locationList(n.key)[nodeIndex]
        offset = self.findEdge(node, e)
        try:
            if offset >= 0:
                raise ValueError, "The edge was already in the node !"
        except ValueError, e:
            print e
            return

        node.adj.append(e)


    def deleteEdge(self, n, e):
        index = self.findNode(n.key)
        try:
            if index < 0:
                raise ValueError, "The node is not in the graph !"
        except ValueError, e:
            print e
            return

        node = self.locationList(n.key)[index]
        offset = self.findEdge(node, e)
        try:
            if offset < 0:
                raise ValueError, "The edge is not in the node !"
        except ValueError, e:
            print e
            return

        del node.adj[offset]


    def locationList(self, key):
        return self.table.locationList(key)


    def traerse(self):
        for r in self.table.hashTable:
            for n in r:
                if n is not None:
                    print n.key,": ",
                    if n.adj != []:
                        for e in n.adj:
                            print e.key,
                print

    def travreseNode(self):
        for r in self.table.hashTable:
            for n in r:
                if n is not None:
                    yield  n


if __name__ == "__main__":
    g = Graph()
    for x in range(10):
        g.addNode(GraphNode(x))
    for x in range(10):
        g.addNode(GraphNode(x))

    print 'hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh'

    for x in range(10):
        g.addEdge(GraphNode(x), GraphNode(x))
        g.addEdge(GraphNode(x),GraphNode(x + 1))
    for x in range(10):
        g.addEdge(GraphNode(x), GraphNode(x))

    g.deleteEdge(GraphNode(9), GraphNode(9))
    g.deleteNode(GraphNode(10))
    g.addEdge(GraphNode(9), GraphNode(100))
    g.deleteNode(GraphNode(100))


    g.traerse()

    print [x.key for x in g.travreseNode()]
