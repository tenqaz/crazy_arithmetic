"""
@author: Jim
@project: crazy_arithmetic
@file: 50_myPow.py
@time: 2019/12/16 16:56
@desc:
    实现 pow(x, n) ，即计算 x 的 n 次幂函数。
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        """

            使用递归解，发现递归的深度是有限的。

            这个不可解

        Args:
            x:
            n:

        Returns:

        """

        if n == 1:
            return x

        if n > 0:
            return x * self.myPow(x, n - 1)
        elif n < 0:
            return 1 / x * self.myPow(x, n + 1)
        else:
            return 1

    def myPow2(self, x: float, n: int) -> float:
        """
            暴力. 使用循环。 leetcode说超过时间限制

        Args:
            x:
            n:

        Returns:

        """

        if n > 0:
            sum = x
            for i in range(n - 1):
                sum *= x
        elif n < 0:
            sum = 1 / x
            for i in range(n + 1, 0):
                sum *= 1 / x
        else:
            sum = 1

        return sum

    def myPow3(self, x: float, n: int) -> float:
        """
            分而治之的方法。

            x * x * x = y
            1. 如果n的个数是偶数
            y = x^(n/2)
            sum = y * y = (x * x)^(n/2)

            2. 如果n的个数是奇数
            y = x^(x//2)
            sum = y * y * x = x * (x * x)^((n-1)/2)

        Args:
            x:
            n:

        Returns:

        """

        if not x:
            return 1

        if n < 0:
            return 1 / self.myPow(x, -n)

        if n % 2:
            return x * self.myPow(x, n - 1)

        return self.myPow(x * x, n / 2)

    def myPow4(self, x: float, n: int) -> float:
        """
            使用位运算，并且不使用递归的方式。 天秀啊。。这种方式我咋想不到呢...

            比myPow3效率高很多。

        Args:
            x:
            n:

        Returns:

        """
        if n < 0:
            x = 1 / x
            n = -n

        pow = 1
        while n:
            if n & 1:
                pow *= x

            x *= x
            n >>= 1


if __name__ == '__main__':
    # 结果: 1024.00
    # x = 2.00000
    # n = 10

    # 结果： 0.25
    x = 2
    n = -2

    # x = 1.00001
    # n = 123456

    solution = Solution()
    rst = solution.myPow3(x, n)

    print(rst)
