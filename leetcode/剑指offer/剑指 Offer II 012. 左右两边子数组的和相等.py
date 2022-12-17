#!/usr/bin/env python
# -*- encoding: utf-8 -*-

#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File: 剑指 Offer II 012. 左右两边子数组的和相等.py
@Time: 2022/12/17 16:43:51
@Author: Jim
@Contact: zhengwenfeng37@gmail.com
@Desc: 

    https://leetcode.cn/problems/tvdfij/
    
    看很多人都说用前缀和解，但是咱并不懂，但时用另一种方式来解。
'''



from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """
            先假设中心下标在最左边，然后比较左右两边的值，如果正确则返回，不正确，将中心下标往右移。
        """
        nums_len = len(nums)
        cur_index = 0
        left_sum = 0

        right_sum = 0
        for i in nums[1:]:
            right_sum += i

        while cur_index < nums_len:
            if left_sum == right_sum:
                return cur_index
            elif cur_index == nums_len - 1:
                return -1

            left_sum += nums[cur_index]
            right_sum -= nums[cur_index + 1]

            cur_index += 1

        return -1

    def pivotIndex2(self, nums: List[int]) -> int:
        """
            前缀和

            2*sum+nums[i]=total
        """
        pass


if __name__ == "__main__":
    # 3
    # nums = [1, 7, 3, 6, 5, 6]

    # -1
    nums = [1, 2, 3]

    # 0
    # nums = [2, 1, -1]

    # 2
    # nums = [-1, -1, -1, -1, -1, 0]

    # 5
    # nums = [-1, -1, 0, 1, 1, 0]
    ret = Solution().pivotIndex(nums)
    print(ret)
