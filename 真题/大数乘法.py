def func(str1: str, str2: str) -> str:
    """
    实现两个大数字符串相乘
    
    Args:
        str1: 第一个数字字符串
        str2: 第二个数字字符串
    
    Returns:
        相乘结果的字符串表示
    
    Time Complexity: O(m*n) where m and n are lengths of str1 and str2
    Space Complexity: O(m+n) for the result array
    """
    # 处理特殊情况：任意一个数为0
    if str1 == "0" or str2 == "0":
        return "0"
    
    len1, len2 = len(str1), len(str2)
    # 结果最多有 len1 + len2 位
    result = [0] * (len1 + len2)
    
    # 从右到左逐位相乘
    for i in range(len1 - 1, -1, -1):
        for j in range(len2 - 1, -1, -1):
            # 计算当前两位的乘积
            mul = int(str1[i]) * int(str2[j])
            
            # 确定乘积在结果数组中的位置
            pos1 = i + j      # 十位位置
            pos2 = i + j + 1  # 个位位置
            
            # 加上当前乘积
            total = mul + result[pos2]
            
            # 处理进位
            result[pos2] = total % 10
            result[pos1] += total // 10
    
    # 转换为字符串并去除前导零
    result_str = ""
    for i, digit in enumerate(result):
        # 跳过前导零，但保留至少一位数字
        if not (i == 0 and digit == 0) or result_str:
            result_str += str(digit)
    
    # 如果结果为空（理论上不会发生），返回"0"
    return result_str if result_str else "0"


# 测试代码
if __name__ == "__main__":
    # 测试用例
    print(func("123", "4567"))  # 应该输出 561741
    print(func("0", "12345"))   # 应该输出 0
    print(func("999", "999"))   # 应该输出 998001