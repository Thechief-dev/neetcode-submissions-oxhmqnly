class MyHashSet:

    def __init__(self):
        self.store = []

    def add(self, key: int) -> None:
        if key not in self.store:
            self.store.append(key)

    def remove(self, key: int) -> None:
        if self.store and key in self.store:
            self.store.remove(key)
        
    def contains(self, key: int) -> bool:
        return key in self.store


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)