"""
@author: Jim
@project: crazy_arithmetic
@file: 509_斐波拉契数.py
@time: 2020/2/17 9:19
@desc:  
    https://leetcode-cn.com/problems/fibonacci-number/
"""


class Solution:
    def fib2(self, N: int) -> int:
        """
            递推

            时间复杂度: O(N)
            空间复杂度: O(1)
        Args:
            N:

        Returns:

        """

        if N <= 1: return N
        if N == 2: return 1

        prev1 = 1
        prev2 = 1

        for i in range(2, N+1):
            prev1, prev2 = prev1 + prev2, prev1

        return prev1

    def fib(self, N: int) -> int:
        """
            递归

            时间复杂度 O(2^N)
            空间复杂度 O(N)
        Args:
            N:

        Returns:

        """

        if N <= 1: return N

        return self.fib(N - 1) + self.fib(N - 2)


if __name__ == '__main__':
    solution = Solution()
    # result = solution.fib(2)  # 1
    # print(result)
    result = solution.fib(3)  # 2
    print(result)
