"""
@author: Jim
@project: crazy_arithmetic
@file: 208_实现Trie(前缀树)(哈希树).py
@time: 2020/1/31 19:45
@desc:  
    
"""


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.end_of_word = "#"

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for char in word:
            node = node.setdefault(char, {})

        node[self.end_of_word] = self.end_of_word

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return self.end_of_word in node

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for char in prefix:
            if char not in node:
                return False

            node = node[char]

        return True

obj = Trie()
obj.insert("apple")

param_2 = obj.search("apple")
print(param_2)

param_3 = obj.startsWith("apple")
print(param_3)

obj.insert("appla")
param_2 = obj.search("apple")
print(param_2)