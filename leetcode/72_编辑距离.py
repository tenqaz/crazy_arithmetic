"""
    https://leetcode.cn/problems/edit-distance/
"""

class Solution:
    def minDistance2(self, word1: str, word2: str) -> int:
        """ 自顶向下 

            使用一个二维数组作为动态规划方程，i和j分别代表着word1和word2的索引

            dp[i][j] 在word1[i] != word2[j]时，有三种状态转换：
              1. 删除. dp[i-1][j] + 1
              2. 替换. dp[i-1][j-1] + 1
              3. 新增. dp[i][j-1]

            如果word1[i] == word2[j]:
              dp[i][j] = dp[i-1][j-1] + 1

        """

        def gen(i, j):
            if i < 0:
                return j+1
            
            if j < 0:
                return i+1
            
            if word1[i] == word2[j]:
                return gen(i-1, j-1)

            return min(
                gen(i-1, j),
                gen(i-1, j-1),
                gen(i, j-1)
            ) + 1
          
        word1_len = len(word1)
        word2_len = len(word2)
        
        return gen(word1_len-1, word2_len-1)
    

    def minDistance3(self, word1: str, word2: str) -> int:
        """ 自顶向下 

            在 minDistance2 的基础上加上缓存进行剪枝。

        """

        word1_len = len(word1)
        word2_len = len(word2)
        cache = [[float('inf') for _ in range(word2_len)] for _ in range(word1_len)]

        def gen(i, j):
            if i < 0:
                return j+1
            
            if j < 0:
                return i+1
            
            if word1[i] == word2[j]:
                return gen(i-1, j-1)
            
            if cache[i][j] != float('inf'):
                return cache[i][j]

            cache[i][j] = min(
                gen(i-1, j),
                gen(i-1, j-1),
                gen(i, j-1)
            ) + 1

            return cache[i][j]
        
        return gen(word1_len-1, word2_len-1)

    def minDistance(self, word1: str, word2: str) -> int:
      """ 自底向上 

          和自顶向下的状态转移方程一样的。需要画一个dp二维表会更直观。

          没有完全理解。没有做出来。
      """
      
      word1_len = len(word1)
      word2_len = len(word2)

      dp = [[float('inf') for _ in range(word2_len)] for _ in range(word1_len)]

      for i in range(1, word1_len):
          dp[i][0] = i
        
      for j in range(word2_len):
          dp[0][j] = j
      

      for i in range(1, word2_len+1):
          for j in range(word1_len+1):
              
              if word1[i-1] == word2[j-1]:
                  dp[i][j] = dp[i-1][j-1]
              else:
                dp[i][j] = min(
                    dp[i-1][j],
                    dp[i-1][j],
                    dp[i][j-1]
                ) + 1

      return dp[word1_len-1][word2_len-1]


if __name__ == '__main__':
    # 3
    word1 = "horse"
    word2 = "ros"
    
    ret = Solution().minDistance(word1, word2)
    print(ret)