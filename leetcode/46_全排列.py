
"""
    https://leetcode.cn/problems/permutations/description/

    思路：
    
    1. 创建tracks列表来记录每一次的路径，并通过判断它的长度与nums的长度得知是否为叶子节点，也就是不能再继续往下走了。
    2. 每次遍历时判断数据是否在tracks中存在，保证不会重复的读取。
    3. 在进入下个节点前，保存路径，从下个节点退出后，再删除路径

"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        self.result = []
        tracks = []

        def gen(tracks):

            if len(tracks) == len(nums):
                self.result.append(tracks.copy())

            for i in nums:

                if i in tracks:
                    continue

                tracks.append(i)

                gen(tracks)

                tracks.pop()

        gen(tracks)

        return self.result
    
if __name__ == '__main__':
    # [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    nums = [1, 2, 3]
    print(Solution().permute(nums))
