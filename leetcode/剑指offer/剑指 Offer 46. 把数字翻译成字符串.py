"""
@author: zwf
@contact: zhengwenfeng37@gmail.com
@time: 2023/7/16 11:00
@desc:
    
"""


class Solution:
    def translateNum(self, num: int) -> int:
        num_str = str(num)
        num_len = len(num_str)
        p, q = 1, 2

        for i in range(2, num_len+1):
            p = p+q  if "10" <= num_str[i-2:i] <= "26":

