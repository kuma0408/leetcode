class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.d = {}

    def get(self, key: int) -> int:
        return self.d[key]

    def put(self, key: int, value: int) -> None:
        self.d[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)