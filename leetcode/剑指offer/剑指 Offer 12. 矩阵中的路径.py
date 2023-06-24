"""
@author: zwf
@contact: zhengwenfeng37@gmail.com
@time: 2023/6/24 20:52
@desc:
    
"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        # 上下左右
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def check(i, j, k):
            if board[i][j] != word[k]:
                return False

            if k == len(word) - 1:
                return True

            visited.add((i, j))
            for p, q in directions:
                next_i, next_j = i + p, j + q
                if (next_i, next_j) in visited or 0 > next_i or next_i >= row_len or 0 > next_j or next_j >= column_len:
                    continue

                if check(next_i, next_j, k + 1):
                    return True

            visited.remove((i, j))

        visited = set()
        row_len = len(board)
        column_len = len(board[0])

        for i in range(row_len):
            for j in range(column_len):
                if check(i, j, 0):
                    return True

        return False


if __name__ == '__main__':
    # True
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"

    # False
    # board = [["a", "b"], ["c", "d"]]
    # word = "abcd"

    s = Solution()
    ret = s.exist(board, word)
    print(ret)