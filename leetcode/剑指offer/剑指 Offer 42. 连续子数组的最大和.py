"""
@author: zwf
@contact: zhengwenfeng37@gmail.com
@time: 2023/7/16 10:14
@desc:
    
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
            1. 数组滚动，当前最大的值
            2. 滚动后的值没有当前值大，则不再滚动，直接从当前值开始滚动
            3. 如果滚动后的值大于最大值，则使用当前滚动的值。
        """
        res = nums[0]

        for i in range(1, len(nums)):
            if nums[i] + nums[i-1] > nums[i]:
                nums[i] += nums[i-1]

            if nums[i] > res:
                res = nums[i]


        return res


if __name__ == '__main__':
    # 6
    print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
