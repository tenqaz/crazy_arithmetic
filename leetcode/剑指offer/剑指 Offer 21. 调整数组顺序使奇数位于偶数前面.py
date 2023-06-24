"""
@author: zwf
@contact: zhengwenfeng37@gmail.com
@time: 2023/6/23 15:08
@desc:
    https://leetcode.cn/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/?envType=study-plan-v2&envId=coding-interviews
"""
from typing import List


class Solution:
    def exchange3(self, nums: List[int]) -> List[int]:
        """
            创建新的数组,遍历nums，将奇数从左插入，偶数从右插入。

            这里用到了python list特性，可以从左右插入，并且会动态扩容。

            时间复杂度：O(n)
            控件复杂度：O(n)

        """

        ret = []

        for num in nums:
            if num % 2 == 0:
                ret.append(num)
            else:
                ret.insert(0, num)

        return ret

    def exchange2(self, nums: List[int]) -> List[int]:
        """
            纯数组特性，而不是用python list特性

            创建新的数组，使用left和right记录数组两端索引，然后遍历，将奇数从左填入，left+1，将偶数从右插入，right-1


            时间复杂度：O(n)
            控件复杂度：O(n)
        """

        n = len(nums)
        left, right = 0, n - 1
        ret_nums = [0] * n
        for num in nums:
            if num % 2 == 0:
                ret_nums[right] = num
                right -= 1
            else:
                ret_nums[left] = num
                left += 1

        return ret_nums

    def exchange(self, nums: List[int]) -> List[int]:
        """
            原地交换，而不是用新的数组.

            时间复杂度：O(n)
            控件福再度: O(1)

            双指针，分别指向左右两端。
            左端开始遍历
            如果左端是奇数，则代表顺序对的，则继续遍历。
            如果左端是偶数，则从右端开始遍历，右端遍历如果是偶数则继续遍历，如果是奇数，则与前端的数进行交换。
        """
        n = len(nums)
        left, right = 0, n-1

        while left < right:
            while right > left and nums[left] % 2 == 1:
                left += 1

            while right > left and nums[right] % 2 == 0:
                right -= 1

            if right > left:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        return nums






if __name__ == '__main__':
    s = Solution()
    ret = s.exchange([1, 2, 3, 4])
    print(ret)
