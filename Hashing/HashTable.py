#  GET HASH VALUE
#  ADD ELEMENT
#  FIND ELEMENT
#  BELOW IS HASH TABLE
# [None, None, None, None, None, None, None, None, None, None,
#  None, None, None, None, None, None, None, None, None, None,
#  None, None, None, 3, None, None, None, None, None, None, 1,
#  None, 2, None, None, None, None, None, None, None, None,
#  None, None, None, None, None, None, None, None, None,
#  None, None, None, None, None, None, None, None, None, None,
#  None, None, None, None, None, None, None, None, None, None, 
#  None, None, None, None, None, None, None, None, None, None, 
#  None, None, None, None, None, None, None, None, None, None, 
#  None, None, None, None, None, None, None, None, None, None]

class HashTable:
    def __init__(self):
        self.max = 100
        self.arr = [None for i in range(self.max)]

    def GetHash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.max
    
    def AddEle(self, key, val):
        h = self.GetHash(key)
        self.arr[h] = val

    def FindEle(self, key):
        h = self.GetHash(key)
        return self.arr[h]

if __name__ == "__main__":
    hashing = HashTable()
    hashing.AddEle("January", 1)
    hashing.AddEle("February", 2)
    hashing.AddEle("march", 3)
    print(hashing.FindEle("February"))
    print(hashing.arr)