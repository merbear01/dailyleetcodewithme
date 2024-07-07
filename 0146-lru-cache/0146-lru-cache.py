from collections import OrderedDict

class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()
        

    def get(self, key):
        if key in self.cache:
            val = self.cache.pop(key)  # pop the value to remove and get it
            self.cache[key] = val  # re-insert to mark it as recently used
            return val
        else:
            return -1
        

    def put(self, key, value):
        if key in self.cache:
            self.cache.pop(key)  # remove the old value
        elif len(self.cache) >= self.capacity:
            self.cache.pop(next(iter(self.cache)))  # remove the first item (least recently used)
        self.cache[key] = value  # insert the new value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
