from Auxiliary_tool import random_list
from Data_structure.HashTable import HashTable

class GraphNode(object):
    def __init__(self, tableSize):
        self.Adj = HashTable(tableSize)
        self.size = self.Adj.tabelSize


class Graph(object):
    def __init__(self, tableSize = 100):
        self.graph = self.init(tableSize)
        self.size = 0

    def init(self, tableSize):
        h = HashTable(tableSize)
        for x in h.hashTable:
            for i in x:
                i.append([])
        return h

    def insertion(self, dot):
        self.graph.insertion(dot)

    def delete(self, dot):
        self.graph.delete(dot)

    def addEdge(self, dot, edge):
        hashVal = self.graph.betterHash(dot)
        index = self.graph.find(hashVal, dot)
        try:
            if index == -1:
                raise "The dot is not in the graph !"
        except ValueError, e:
            print e

        self.graph.hashTable[hashVal][index].append(edge)

    def findDot(self, dot):
        hashVal = self.graph.betterHash(dot)
        return self.graph.find(hashVal, dot)

    def findEdge(self, dot, edge):
        pass

    def delEdge(self, dot, edge):
        hashVal = self.graph.betterHash(dot)
        index = self.graph.find(hashVal, dot)
        adjTable = self.graph.hashTable[hashVal][index]
        if index == -1:
            print "The dot is not in the graph !"
        else:
            for x in adjTable:
                pass
            self.graph.hashTable[hashVal][index].append(edge)















