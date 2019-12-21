"""
@author: Jim
@project: crazy_arithmetic
@file: LRUCache.py
@time: 2019/12/21 17:46
@desc:

    LRU实现

    使用OrderedDict数据结构来实现该算法。OrderedDict是一个有序的字典。
"""

from collections import OrderedDict


class LRUCache:

    def __init__(self, init_size=5):

        self.init_size = init_size
        self.cache = OrderedDict()

    def get(self, key):
        """
        如果存在，将该key对应的值拿到并返回，然后将该值放在字典中的第一位。
        """

        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value
        else:
            value = None

        return value

    def set(self, key, value):
        """
        如果存在，则拿到该值并放到字典中第一位。如果缓存已满，则删除最后一位，将新添加的值加到第一位。
        :param key:
        :param value:
        :return:
        """

        if key in self.cache:  # 已存在
            self.cache.pop(key)
        elif len(self.cache) == self.init_size:  # 缓存已满
            self.cache.popitem(last=False)

        self.cache[key] = value

    def __str__(self):
        return ",".join(self.cache)


if __name__ == '__main__':
    lru = LRUCache(init_size=3)

    lru.set("a", 1)
    lru.set("b", 2)
    print(lru)
    lru.set("c", 3)
    lru.set("d", 4)
    value = lru.get("c")
    print("value = {}".format(value))
    print(lru)
    lru.set("e", 5)
    lru.set("f", 6)
    value = lru.get("d")
    print("value = {}".format(value))
    print(lru)
    lru.set("g", 7)
