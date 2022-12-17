#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File: 剑指 Offer II 006. 排序数组中两个数字之和.py
@Time: 2022/12/17 13:51:19
@Author: Jim
@Contact: zhengwenfeng37@gmail.com
@Desc: 
    https://leetcode.cn/problems/kLl5u1/

    和15题一样
'''


from typing import List


class Solution:
    def twoSum3(self, numbers: List[int], target: int) -> List[int]:
        """双指针"""
        p, q = 0, len(numbers) - 1

        while p < q:
            if numbers[p] + numbers[q] == target:
                return [p, q]
            elif numbers[p] + numbers[q] < target:
                p += 1
            else:
                q -= 1

    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        """ 二分法 """

        max_len = len(numbers)

        for i in range(max_len):

            left = i + 1
            right = max_len - 1

            while left <= right:
                mid = (right - left) // 2 + left
                if numbers[mid] == target - numbers[i]:
                    return [i, mid]
                elif numbers[mid] < target - numbers[i]:
                    left = mid+1
                else:
                    right = mid-1

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
            哈希法
        """
        cache_dict = {}
        for index, value in enumerate(numbers):
            expected = target - value
            if expected in cache_dict:
                return [cache_dict[expected], index]
            else:
                cache_dict[value] = index

    def twoSum_me(self, numbers: List[int], target: int) -> List[int]:
        """
            i=0, j=len(numbers)-1

            如果 numbers[i] + numbers[j] == target  return
            如果 numbers[i] + numbers[j] > target  那么 q -= 1
            如果 numbers[j] + numbers[j] < target  那么 p += 1

            leetcode超时
        """
        max_len = len(numbers)

        for i in range(max_len):
            for j in range(max_len - 1, i, -1):
                if numbers[i] + numbers[j] == target:
                    return [i, j]
                elif numbers[i] + numbers[j] > target:
                    continue
                elif numbers[i] + numbers[j] < target:
                    break


if __name__ == '__main__':
    # [1,3]
    numbers = [1, 2, 4, 6, 10]
    target = 8

    # [0,2]
    # numbers = [2, 3, 4]
    # target = 6
    ret = Solution().twoSum3(numbers, target)
    print(ret)
