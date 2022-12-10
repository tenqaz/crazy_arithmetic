"""
    https://leetcode-cn.com/problems/number-of-islands/

    
    给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

    岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

    此外，你可以假设该网格的四条边均被水包围。

"""

from typing import List, Mapping


class BingChaJi:

    def __init__(self):
        pass
        
    
    def find(self):
        pass

    def union(self):
        pass


class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        """
            并查集解法
        """
        pass


    def dfs(self, i, j, grid):
        """
            将附近的1都置位0
        """
        try:
            if grid[i][j] == "0" or i < 0 or j < 0:
                return
        except IndexError:
            return
            

        grid[i][j] = "0"

        # 上
        self.dfs(i-1, j, grid) 

        # 下
        self.dfs(i+1, j, grid)

        # 左
        self.dfs(i, j-1, grid)

        # 右
        self.dfs(i, j+1, grid)

    def numIslands2(self, grid: List[List[str]]) -> int:
        """ 
            dfs解法

            循环每个元素，如果是陆地，计数+1，将其置为海洋，再搜索其四周是否为陆地，递归查询做相同操作.
        """
        count = 0
        row_num = len(grid)
        col_num = len(grid[0])
        
        for i in range(row_num):
            for j in range(col_num):
                record = grid[i][j]
                if record == "1":
                    count += 1
                    self.dfs(i, j, grid)

        return count


# rst = 1
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

# rst = 3
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

# rst = 1
grid = [
    ["1","1","1"],
    ["0","1","0"],
    ["1","1","1"]
]

# rst = 3
grid = [
    ["1","0","1","1","0","1","1"]
]

solution = Solution()
ret = solution.numIslands(grid)
print(ret)