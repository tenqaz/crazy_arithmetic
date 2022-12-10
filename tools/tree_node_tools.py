"""
    二叉树的构造与打印公共方法
"""


from pip import main


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def print_Treelist(head: TreeNode):
    queue = [head]
    print(head.val, end=",")

    while queue:

        for _ in queue:
            node = queue.pop(0)

            # if node.left:
            #     queue.append(node.left)
            #
            # if node.right:
            #     queue.append(node.right)

            # if not node.left and not node.right:
            #     continue

            if node.left:
                queue.append(node.left)
                print(node.left.val, end=",")
            else:
                print(None, end=",")

            if node.right:
                queue.append(node.right)
                print(node.right.val, end=",")
            else:
                print(None, end=",")



def make_Treelist(value_list):
    head = TreeNode(value_list.pop(0))

    queue = [head]

    while queue:

        for _ in queue:
            node = queue.pop(0)

            if not value_list:
                break

            try:
                left_val = value_list.pop(0)
                if left_val:
                    left_node = TreeNode(left_val)
                    node.left = left_node
                    queue.append(left_node)
            except IndexError:
                pass

            try:
                right_val = value_list.pop(0)
                if right_val:
                    right_node = TreeNode(right_val)
                    node.right = right_node
                    queue.append(right_node)
            except IndexError:
                pass

    return head

if __name__ == '__main__':
    root = [3, 9, 20, None, None, 15, 7]
    head = make_Treelist(root)

    # [3,9,20,None,None,15,7]
    print_Treelist(head)