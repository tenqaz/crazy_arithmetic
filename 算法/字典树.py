"""
@author: Jim
@project: crazy_arithmetic
@file: 字典树.py
@time: 2021/9/20 18:06
@desc:  

"""


class DictTree:

    def __init__(self):
        self.data = {}
        self.end = "#"

    def insert(self, key):
        data = self.data
        for i in key:
            data = data.setdefault(i, {})

        data[self.end] = True

    def insert_many(self, key_list):
        for key in key_list:
            self.insert(key)

    def find(self, key):
        data = self.data
        for i in key:
            data = data.get(i)
            if data is None:
                return False

        if self.end not in data:
            return False

        return True

d = DictTree()
d.insert("zhangsan")
ret = d.find("zhangsa")
print(ret)