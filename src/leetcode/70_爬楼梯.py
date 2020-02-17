"""
@author: Jim
@project: crazy_arithmetic
@file: 70_爬楼梯.py
@time: 2020/2/2 19:44
@desc:  
    https://leetcode-cn.com/problems/climbing-stairs/description/
"""


class Solution:

    def climbStairs2(self, n: int) -> int:
        """
            动态规划

            f(n) = f(n-1) * f(n-2)
            斐波拉契数列.

            时间复杂度: O(n)
            空间复杂度: O(n)
        Args:
            n:

        Returns:

        """
        if n == 0 or n == 1 or n == 2: return n

        mem = [1, 2]
        for i in range(2, n):
            mem.append(mem[i - 1] + mem[i - 2])

        return mem[n - 1]

    def climbStairs(self, n: int) -> int:
        """
            使用更简洁的方式. 更优解.

            时间复杂度: O(n)
            空间复杂度: O(1)
        Args:
            n:

        Returns:

        """

        x, y = 1, 1
        for i in range(1, n):
            x, y = y, x + y

        return y


if __name__ == '__main__':
    solution = Solution()
    result = solution.climbStairs(3)
    print(result)
