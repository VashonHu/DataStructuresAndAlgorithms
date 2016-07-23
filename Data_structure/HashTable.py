from Auxiliary_tool import NextPrimary

class HashTable(object):
    def __init__(self, tabelSize=100):
        self.hashTable = []
        self.tabelSize = self.realSize(tabelSize)

    def realSize(self, size):
        size = NextPrimary.nextPrimary(size)
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
            if x == k:
                return index
            index += 1
        return -1

    def insertion(self, k):
        hashVaule = self.betterHash(k)
        repeatTable = self.hashTable[hashVaule]
        if self.find(hashVaule, k) == -1 :
            repeatTable.append(k)

    def delete(self, k):
        hashValue = self.betterHash(k)
        repeatTable = self.hashTable[hashValue]
        index = self.find(hashValue, k)
        if index == -1:
            print "The key is not in the hashtable !"
        else:
            del repeatTable[index]


    def traerse(self):
        for i in self.hashTable:
            for j in i:
                if j is not None:
                    print j,
            print

if __name__ == "__main__":
    h = HashTable()
    for x in range(100):
        h.insertion(x)

    for x in range(70):
        h.delete(x)

    h.traerse()

