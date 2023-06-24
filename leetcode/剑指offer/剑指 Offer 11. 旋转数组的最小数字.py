"""
@author: zwf
@contact: zhengwenfeng37@gmail.com
@time: 2023/6/24 12:48
@desc:
    https://leetcode.cn/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/?envType=study-plan-v2&envId=coding-interviews
"""
from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        """
            遍历

            时间复杂度：O(n)
            空间复杂度：O(1)

        """
        last_num = numbers[0]
        for num in numbers[1:]:
            if num >= last_num:
                last_num = num
            else:
                return num

        return numbers[0]


if __name__ == '__main__':
    s = Solution()
    # numbers = [3, 4, 5, 1, 2]
    numbers = [1, 3, 5]
    ret = s.minArray(numbers)
    print(ret)
