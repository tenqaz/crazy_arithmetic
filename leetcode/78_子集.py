"""
    思路：
    1. 使用回溯
    2. 通过start来保证树枝不会有重复值。
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        tracks = []

        def gen(tracks, start):
            self.result.append(tracks.copy())

            for i in range(start, len(nums)):
                tracks.append(nums[i])

                gen(tracks, i + 1)

                tracks.pop()

        gen(tracks, 0)
        return self.result

if __name__ == '__main__':
    # [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    nums = [1, 2, 3]
    print(Solution().subsets(nums))
