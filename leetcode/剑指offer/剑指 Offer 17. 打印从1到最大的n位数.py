"""
@author: zwf
@contact: zhengwenfeng37@gmail.com
@time: 2023/6/25 19:20
@desc:
    
"""
from typing import List


class Solution:
    def printNumbers(self, n: int) -> List[int]:
        ret = []
        for i in range(1, 10 ** n):
            ret.append(i)

        return ret


if __name__ == '__main__':
    print(Solution().printNumbers(2))
