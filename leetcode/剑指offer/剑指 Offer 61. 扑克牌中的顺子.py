"""
@author: zwf
@contact: zhengwenfeng37@gmail.com
@time: 2023/6/25 20:18
@desc:
    
"""
from typing import List


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        nums.sort()

        skip_count = 0
        start_flag = False
        cur_num = 0
        for num in nums:
            if num == 0:
                skip_count += 1
                continue

            if not start_flag:
                cur_num = num
                start_flag = not start_flag
                continue

            if cur_num == num:
                return False

            cur_num += 1
            if cur_num == num:
                continue

            if skip_count != 0:
                skip_count -= 1
                continue

            return False

        return True


if __name__ == '__main__':
    print(Solution().isStraight([1,2,12,0,3]))
