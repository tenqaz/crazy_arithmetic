"""
    实现一个计算器
    (1+2*8)*3+2+23*12+12/4+(2+(3+12*6))
"""


def mid2post(trans_string, op_rank):
    """
        中缀表达式转后缀表达式
        1. 如果是数字，如果是双位则需要组合在一起，然后再append到post_list中，单数直接append
        2. 如果是(直接append到栈中
        3. 如果是）则需要出栈获取里面所有的操作符
        4. 如果是运算符，则需要判断优先级，优先级高的则出栈到post_list中。
    """
    stack = []
    post_list = []
    i = 0
    trans_string_len = len(trans_string)
    while i < trans_string_len:
        if is_digit(trans_string[i]):
            n = int(trans_string[i])
            i += 1
            while i < trans_string_len and is_digit(trans_string[i]):
                n = n * 10 + int(trans_string[i])
                i += 1

            post_list.append(str(n))
        else:
            # 运算符
            if trans_string[i] == "(":
                stack.append("(")
            elif trans_string[i] == ")":
                while stack and stack[-1] != "(":
                    post_list.append(stack.pop())

                # (弹出不需要
                stack.pop()
            else:
                # 其他的运算符
                while stack and op_rank[trans_string[i]] <= op_rank[stack[-1]]:
                    post_list.append(stack.pop())

                stack.append(trans_string[i])

            i += 1

    while stack:
        post_list.append(stack.pop())

    return "".join(post_list)


def calc_by_post(post_str):
    """
        后缀表达式计算

        遇到操作符，则出栈两个并进行运算，然后再将结果入栈，最后栈中的结果，即为答案。
    """

    stack = []
    for i in post_str:
        if is_digit(i):
            stack.append(i)
        else:
            v2 = int(stack.pop())
            v1 = int(stack.pop())
            if i == "+":
                v3 = v1 + v2
            elif i == "-":
                v3 = v1 - v2
            elif i == "*":
                v3 = v1 * v2
            elif i == "/":
                v3 = v1 / v2

            stack.append(v3)

    return stack.pop()


def is_digit(char):
    return "0" <= char <= "9"


if __name__ == '__main__':
    op_rank = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}
    string_list = ['1+2', '1+2*3', '(1+2)*3', '(1+2)*(3+4)', '1+2+3+4']
    for trans_str in string_list:
        print("%s => %s => %d" % (trans_str, mid2post(trans_str, op_rank), calc_by_post(mid2post(trans_str, op_rank))))

    # 输出
    # 1 + 2 = > 12 + = > 3
    # 1 + 2 * 3 = > 123 * + = > 7
    # (1 + 2) * 3 = > 12 + 3 * = > 9
    # (1 + 2) * (3 + 4) = > 12 + 34 + * = > 21
    # 1 + 2 + 3 + 4 = > 12 + 3 + 4 + = > 10

    # trans_str = "1+2+3+4"
    # print("%s => %s" % (trans_str, mid2post(trans_str, op_rank)))
