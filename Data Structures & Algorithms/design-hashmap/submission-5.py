class LinkedList:
    def __init__(self, key = -1, value = -1, next = None):
        self.value = value
        self.key = key
        self.next = next

class MyHashMap:

    def __init__(self):
        self.store = [LinkedList() for _ in range(10000)]
        
    def hashing(self, key):
        return key % len(self.store)

    def put(self, key: int, value: int) -> None:
        node = self.store[self.hashing(key)]

        while node.next:
            if node.next.key == key:
                node.next.value = value
                return
            node = node.next
        node.next = LinkedList(key, value)

    def get(self, key: int) -> int:
        node = self.store[self.hashing(key)]
        
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return -1
        

    def remove(self, key: int) -> None:
        node = self.store[self.hashing(key)]
        
        while node.next:
            if node.next.key == key:
                node.next = node.next.next
                return
            node = node.next
        

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)