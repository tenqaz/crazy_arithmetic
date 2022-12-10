"""
https://leetcode-cn.com/problems/power-of-two/


"""
class Solution:

    def isPowerOfTwo3(self, n: int) -> bool:
        """ 位运算

            1 2
            10 2
            100 4 
            1000 8
            10000 16

            如上所述，2的幂的二进制仅包含一个1.
            计算1的个数是否为1
        """

        count = 0

        while n:
            if n & 1 == 1:
                count += 1

            n = n >> 1

            if count > 1:
                return False

        if count == 0:
            return False

        return True

    def isPowerOfTwo2(self, n: int) -> bool:
        """ 位运算(推荐)

            1 2
            10 2
            100 4 
            1000 8
            10000 16

            如上所述，2的幂的二进制仅包含一个1。
            计算1的个数是否为1
        """
        if n == 0:
            return False

        count = 0

        for i in range(2):
            count += 1
            n = n & (n-1)
            if n == 0:
                break

        if count != 1:
            return False

        return True
        

    def isPowerOfTwo(self, n: int) -> bool:
        """ 暴力破解
        """

        if n == 0:
            return False

        while n:

            if n % 2 != 0 and n != 1:
                return False

            n //= 2

        return True

s = Solution()
ret = s.isPowerOfTwo3(3)
print(ret)