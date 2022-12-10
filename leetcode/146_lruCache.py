"""
@author: Jim
@project: crazy_arithmetic
@file: 146_lruCache.py
@time: 2020/2/16 17:20
@desc:  
    https://leetcode-cn.com/problems/lru-cache/#/

    python 直接使用 OrderedDict这个有序的字典实现，如果是C++得使用双向链表解决
"""

from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        """
            获取key的值
        Args:
            key:

        Returns:

        """
        if key not in self.cache: return -1

        value = self.cache.pop(key)
        self.cache[key] = value

        return value

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.cache.pop(key)
            self.cache[key] = value
        else:
            if len(self.cache) == self.capacity:
                self.cache.popitem(last=False)

            self.cache[key] = value


cache = LRUCache(2)

cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))  ## returns 1
cache.put(3, 3)  # evicts key 2
print(cache.get(2))  # returns -1 (not found)
cache.put(4, 4)    # evicts key 1
print(cache.get(1))       # returns -1 (not found)
print(cache.get(3))       # returns 3
print(cache.get(4))       # returns 4
