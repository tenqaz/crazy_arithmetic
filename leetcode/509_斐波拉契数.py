"""
@author: Jim
@project: crazy_arithmetic
@file: 509_斐波拉契数.py
@time: 2020/2/17 9:19
@desc:  
    https://leetcode-cn.com/problems/fibonacci-number/
"""


class Solution:

    def fib2(self, n: int) -> int:
        """
            使用暴力递推的方式。

            其问题是，会有重复的值进行计算。
        """
        if n == 1 or n == 2:
            return 1

        return self.fib(n - 1) + self.fib(n - 2)

    def fib3(self, n: int) -> int:
        """  暴力递推，添加一个缓存，重复的N不进行重复进行计算
        """

        cache = {}

        def gen(n):

            if n == 1 or n == 2:
                return 1

            if n in cache:
                return cache[n]

            cache[n] = gen(n - 1) + gen(n - 2)
            return cache[n]

        return gen(n)

    def fib4(self, n: int) -> int:
        """ 通过动态规划递推的方式。
        """
        if n == 0:
            return 0

        dp = [0] * (n + 1)

        dp[1] = dp[2] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

    def fib(self, n: int) -> int:
        """ 不通过创建dp数组的方式
            空间复杂度为O(1)
        """
        if n <= 1:
            return n

        if n == 2:
            return 1

        pre1 = pre2 = 1

        for i in range(2, n):
            pre1, pre2 = pre1 + pre2, pre1

        return pre1


if __name__ == '__main__':
    solution = Solution()
    # result = solution.fib(2)  # 1
    # print(result)

    result = solution.fib3(3)  # 2
    print(result)
