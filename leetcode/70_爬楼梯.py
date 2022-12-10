"""
@author: Jim
@project: crazy_arithmetic
@file: 70_爬楼梯.py
@time: 2020/2/2 19:44
@desc:  
    https://leetcode-cn.com/problems/climbing-stairs/description/
"""


class Solution:

    def climbStairs(self, n: int) -> int:
        """
            动态规划。

            从终点开始算
            
            f(n)=终点的走法个数
            前一步和前两步走法的总和
            f(n) = f(n-1) + f(n-2)

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

    def climbStairs2(self, n: int) -> int:
        """ 
            动态规划+滚动数组

            比较climbStairs解法，节省了mem空间，O(1)的空间复杂度
        """

        if n == 0 or n == 1 or n == 2: return n

        x = 1  # 第一阶台阶走法个数
        y = 2  # 第二阶台阶走法个数

        # 每次循环，x,y,res都会往后走一次。
        for i in range(2, n):
            x, y = y, x+y

        return y


if __name__ == '__main__':
    solution = Solution()
    result = solution.climbStairs2(3)
    print(result)
