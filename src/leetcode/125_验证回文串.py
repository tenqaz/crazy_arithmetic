"""
@author: Jim
@project: crazy_arithmetic
@file: 125_验证回文串.py
@time: 2021/9/20 17:48
@desc:  
    
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """ 双指针

        Args:
            s:

        Returns:

        """

        left = 0
        right = len(s) - 1

        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            elif not s[right].isalnum():
                right -= 1
                continue

            if s[left].upper() != s[right].upper():
                return False

            left += 1
            right -= 1

        return True


data = "A man, a plan, a canal: Panama"
s = Solution()
ret = s.isPalindrome(data)
print(ret)
