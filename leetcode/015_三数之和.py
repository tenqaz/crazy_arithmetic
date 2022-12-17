"""
@author: Jim
@project: crazy_arithmetic
@file: 015_三数之和.py
@time: 2019/12/10 11:31
@desc:

    有一种方式使用双指针形式:
    首先排序使用快排: O(nlogn)，然后遍历nums, 从遍历a的下一个开始用两个指针指向首端b和末端c
        当 a + b + c > 0，则末端C向左移动一步，然后继续比较
        当 a + b + c < 0. 则首端向右移动一步，然后继续比较
        当 a + b + c = 0. 则ok

    和剑指offer007题目一样

"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """ 排序 + 双指针

            时间复杂度:O(n^2)
            空间复杂度:O(1)
        """

        ret = []
        n = len(nums)
        nums.sort()

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            if nums[i] > 0:
                break

            L = i + 1
            R = n - 1
            while L < R:
                if nums[i] + nums[L] + nums[R] == 0:
                    ret.append([nums[i], nums[L], nums[R]])
                    while L < R and nums[L] == nums[L + 1]:
                        L += 1

                    while L < R and nums[R] == nums[R - 1]:
                        R -= 1

                    L += 1
                    R -= 1
                elif nums[i] + nums[L] + nums[R] < 0:
                    L += 1
                else:
                    R -= 1

        return ret

    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        """

            使用哈希表完成。类似于两数之和

            时间复杂度: O(n^2)
            空间复杂度: On(n)

        Args:
            nums:

        Returns:

        """

        if len(nums) < 3:
            return []

        nums.sort()
        res = set()
        for i, v in enumerate(nums[:-2]):
            if i >= 1 and v == nums[i - 1]:
                continue

            d = {}

            for x in nums[i + 1:]:
                if x not in d:
                    d[-v - x] = 1
                else:
                    res.add((v, -v - x, x))
        return map(list, res)


    def threeSum_99(self, nums: List[int]) -> List[List[int]]:
        """ 暴力破解

            该放在leetcode上直接超时。
        """
        ret = []
        nums.sort()
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i+1, len(nums)):
                if j != i+1 and nums[j] == nums[j - 1]:
                    continue

                for k in range(j+1, len(nums)):
                    if k != j+1 and nums[k] == nums[k-1]:
                        continue

                    if nums[i] + nums[j] + nums[k] == 0:
                        ret.append([nums[i], nums[j], nums[k]])

        return ret

if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    solution = Solution()
    rst = solution.threeSum2(nums)
    print(list(rst))
