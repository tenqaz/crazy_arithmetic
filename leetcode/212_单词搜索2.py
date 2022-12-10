"""
    https://leetcode-cn.com/problems/word-search-ii/

    解法： 
    1. DFS
    2. trie + dfs
"""
from typing import List

class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        pass
       
                            


# 预期: ["oath", "eat"]
# board = [
#     ["o","a","a","n"],
#     ["e","t","a","e"],
#     ["i","h","k","r"],
#     ["i","f","l","v"]
# ]
# words = ["oath","pea","eat","rain"]

# 预期：[]
# board = [["a","a"]]
# words = ["aaa"]

# 预期: abbbababaa
# board = [
#     ["b","b","a","a","b","a"],
#     ["b","b","a","b","a","a"],
#     ["b","b","b","b","b","b"],
#     ["a","a","a","b","a","a"],
#     ["a","b","a","a","b","b"]
# ]
# words = ["abbbababaa"]

# 预期: ["eaabcdgfa","eaafgdcba"]
# board = [
#     ["a","b","c"],
#     ["a","e","d"],
#     ["a","f","g"]
# ]
# words = ["eaafgdcba","eaabcdgfa"]

# 预期: ["a"]
# board = [["a"]]
# words = ["a"]

# 预期: []
board = [["a"]]
words = ["ab"]

s = Solution()
ret = s.findWords(board, words)
print(ret)