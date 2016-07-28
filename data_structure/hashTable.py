from auxiliary_tool.nextPrimary import nextPrimary

class TabelNode(object):
    def __init__(self, key):
        self.key = key

class HashTable(object):
    def __init__(self, tabelSize=100):
        self.hashTable = []
        self.tabelSize = self.realSize(tabelSize)

    def realSize(self, size):
        size = nextPrimary(size)
        for x in range(size):
            self.hashTable.append([])
        return size

    def betterHash(self, k):
        return hash(k) % self.tabelSize

    def find(self, hashVaule, k):
        repeatTable = self.hashTable[hashVaule]
        if repeatTable is None:
            return -1
        index = 0
        for x in repeatTable:
            if x.key == k:
                return index
            index += 1
        return -1

    def insertion(self, item):
        hashVaule = self.betterHash(item.key)
        repeatTable = self.hashTable[hashVaule]
        if self.find(hashVaule, item.key) == -1 :
            repeatTable.append(item)

    def delete(self, item):
        hashValue = self.betterHash(item.key)
        repeatTable = self.hashTable[hashValue]
        index = self.find(hashValue, item.key)
        if index == -1:
            print "The key is not in the hashtable !"
        else:
            del repeatTable[index]


    def traerse(self):
        for r in self.hashTable:
            for n in r:
                if n is not None:
                    print n.key,
                print

    def locationList(self, k):
        hashVal = self.betterHash(k)
        return self.hashTable[hashVal]

if __name__ == "__main__":
    h = HashTable()
    for x in range(10):
        h.insertion(TabelNode(x))

    for x in range(9):
        h.delete(TabelNode(x))

    h.traerse()

