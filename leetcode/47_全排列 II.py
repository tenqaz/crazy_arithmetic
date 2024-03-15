from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """自己想的
            1. 回溯
            2. 使用used来记录nums中使用过的下标，然后不能再次被使用。
            3. 使用tracks和resuly比较，防止有重复数据
        """

        self.result = []
        tracks = []
        used = [False] * len(nums)

        def gen(tracks):
            if len(tracks) == len(nums):

                if tracks in self.result:
                    return

                self.result.append(tracks.copy())
                return

            for i in range(len(nums)):

                if used[i]:
                    continue

                tracks.append(nums[i])
                used[i] = True

                gen(tracks)

                used[i] = False
                tracks.pop()

        gen(tracks)
        return self.result