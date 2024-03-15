"""
    https://leetcode.cn/problems/subsets-ii/description/

    思路：
        1. 回溯
        2. start用来控制不会重复
        
        3. 最重要的是，需要先通过排序，然后再判断如果是重复数字则跳过。
"""

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        tracks = []

        def gen(tracks, start):

            self.result.append(tracks.copy())

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue

                tracks.append(nums[i])

                gen(tracks, i + 1)

                tracks.pop()

        nums.sort()
        gen(tracks, 0)
        return self.result