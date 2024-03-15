"""
    https://leetcode.cn/problems/combination-sum-ii/description/

    思路:
    1. 回溯
    2. 使用start进行剪枝
    3. 计算求和与target比较作为判断条件
    4. 使用排序，然后再去重
"""

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        self.result = []
        tracks = []

        def gen(tracks, start):

            if sum(tracks) == target:
                self.result.append(tracks.copy())
                return

            if sum(tracks) > target:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                tracks.append(candidates[i])

                gen(tracks, i + 1)

                tracks.pop()

        candidates.sort()
        gen(tracks, 0)
        return self.result