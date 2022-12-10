class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_linkedlist(head: ListNode):
    print("--------分割线------")
    while head:
        print(head.val)
        head = head.next


def make_linkedlist(value_list):
    if not value_list:
        return

    head = ListNode(value_list[0])
    cur_node = head

    for i in value_list[1:]:
        node = ListNode(i)
        cur_node.next = node
        cur_node = node

    return head