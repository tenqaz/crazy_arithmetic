"""

新增和删除的操作时一致的

dp[i][j] = if 两个字符相同
              min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])+1
            else
             min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])+1

"""