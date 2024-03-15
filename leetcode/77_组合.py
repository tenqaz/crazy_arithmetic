"""
    思路：
    1. 回溯
    2. 使用start来保证不会重复
    3. 判断tracks路径长度与k相等时保存结果。
"""
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        self.result = []
        tracks = []

        def gen(tracks, start):
            if len(tracks) == k:
                self.result.append(tracks.copy())
                return

            for i in range(start, n + 1):

                tracks.append(i)

                gen(tracks, i+1)

                tracks.pop()

        gen(tracks, 1)

        return self.result
    
if __name__ == '__main__':
    # [[2, 4],[3, 4],[2, 3],[1, 2],[1, 3],[1, 4]]
    n = 4
    k = 2

    print(Solution().combine(n, k))