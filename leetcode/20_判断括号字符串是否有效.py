"""
@author: Jim
@project: crazy_arithmetic
@file: 20_判断括号字符串是否有效.py
@time: 2019/12/1 15:59
@desc:

判断括号字符串是否有效


"""


class Solution(object):
    def isValid(self, s: str) -> bool:
        """
            有效的括号

        :type s: str
        :rtype: bool
        """

        stack_list = []
        mapping = {"}": "{", "]": "[", ")": "("}

        for i in s:
            if i in mapping:

                pop_value = stack_list.pop() if stack_list else "#"
                
                # 可以提前结束
                if pop_value != mapping[i]:
                    return False
            else:
                stack_list.append(i)

        return not stack_list

    def isValid2(self, s: str) -> bool:
        stack = []
        mapping = {
            "}": "{",
            ")": "(",
            "]": "["
        }

        for i in s:
            if i in mapping:
                if not stack:
                    return False
                    
                v = stack.pop()
                if mapping[i] != v:
                    return False
            else:
                stack.append(i)

        if stack:
            return False
        else:
            return True
            
                
        

if __name__ == '__main__':
    solution = Solution()
    rst = solution.isValid("{([[]])}")
    print(rst)
