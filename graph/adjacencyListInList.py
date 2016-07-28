'''
    list1       ----hashTable
        list2       ---repeatTable
            list3       ---list[0] is dot, list[1]...list[n] is its edge

    !!!!!! this program is not finished, because it is not meets the demand of BFS

'''

from auxiliary_tool import random_list
from auxiliary_tool.nextPrimary import nextPrimary
from data_structure.hashTable import HashTable
import sys


class Graph(object):
    def __init__(self, tableSize=100):
        self.graph = self.init(tableSize)

    def init(self, tableSize):
        h = HashTable(tableSize)
        return h

    def addDot(self, dot):
        result = self.findDot(dot)
        try:
            if result[0] >= 0:
                raise ValueError, "The dot was already in the graph !"
        except ValueError, e:
            print e
            return
        adjTable = [dot]
        result[1].append(adjTable)

    def deleteDot(self, dot):
        result = self.findDot(dot)
        try:
            if result[0] < 0:
                raise ValueError, "The dot is not in the graph !"
        except ValueError, e:
            print e
            return
        del result[1][result[0]]

    def addEdge(self, dot, edge):
        resultDot = self.findDot(dot)
        try:
            if resultDot[0] < 0:
                raise ValueError, "The dot is not in the graph !"
        except ValueError, e:
            print e
            return

        dotTable = resultDot[1]
        resultEdge = self.findEdge(dotTable, edge)
        try:
            if resultEdge[0] >= 0:
                raise ValueError, "The edge was already in the adjTable of the dot !"
        except ValueError, e:
            print e
            return
        dotTable.append(edge)

    def findDot(self, dot):
        hashVal = self.graph.betterHash(dot)
        repeatTable = self.graph.hashTable[hashVal]
        if repeatTable == []:
            return (-1, repeatTable)
        index = 0  # relate repeatTable
        for x in repeatTable:
            if x[0] == dot:
                return (index, repeatTable)
            index += 1
        return (-1, repeatTable)  # [0] means the index or the signal of the error, [1] means the repeatTable

    def findEdge(self, dotTable, edge):
        offset = 1
        if len(dotTable) < 2:
            return (-1, dotTable)
        for x in dotTable[1:]:
            if x == edge:
                return (offset, dotTable)
            offset += 1
        return (-1, dotTable)

    def delEdge(self, dot, edge):
        pass

    def traverse(self):
        for r in self.graph.hashTable:
            for adj in r:
                if adj != []:
                    print adj[0], ': ',
                    if len(adj) > 1:
                        for edge in adj:
                            print edge,
                    print


if __name__ == "__main__":
    g = Graph()
    for x in range(10):
        g.addDot(x)

    g.traverse()

    print 'gggggggggggggggggggggggggggggggggggggggg'

    for x in range(12):
        g.deleteDot(x)

    g.traverse()















