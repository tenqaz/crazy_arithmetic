"""
@author: Jim
@project: crazy_arithmetic
@file: 69_X的平方根.py
@time: 2020/1/31 18:19
@desc:  
    https://leetcode-cn.com/problems/sqrtx/
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        """
            二分法

        Args:
            x:

        Returns:

        """

        if x == 0 or x == 1: return x

        left, right = 1, x

        res = x

        while left <= right:

            mid = (left + right) // 2

            if mid * mid > x:
                right = mid - 1
            elif mid * mid < x:
                left = mid + 1
                res = mid
            else:
                res = mid
                break

        return int(res)





if __name__ == '__main__':
    solution = Solution()
    result = solution.mySqrt(4)
    print(result)
