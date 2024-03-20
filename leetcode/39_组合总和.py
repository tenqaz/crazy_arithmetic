"""
    https://leetcode.cn/problems/combination-sum/description/

    思路：
    1. 回溯

"""
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        self.result = []
        tracks = []

        def gen(tracks, start):

            if sum(tracks) == target:
                self.result.append(tracks.copy())
                return

            for i in range(start, len(candidates)):
                if sum(tracks) + candidates[i] > target:
                    continue

                tracks.append(candidates[i])
                gen(tracks, i)
                tracks.pop()


        gen(tracks, 0)
        return self.result


if __name__ == '__main__':
    # 输出：[[2, 2, 3], [7]]
    candidates = [2, 3, 6, 7]
    target = 7

    print(Solution().combinationSum(candidates, target))