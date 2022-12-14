#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File: 剑指offer0二_027_回文链表.py
@Time: 2022/12/14 13:16:41
@Author: Jim
@Contact: zhengwenfeng37@gmail.com
@Desc: 
    判断链表是否为回文链表
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        cache_list = []
        tmp_head = head

        while tmp_head:
            cache_list.append(tmp_head.val)
            tmp_head = tmp_head.next
        
        while head:
            if head.val != cache_list.pop():
                return False
            head = head.next

        return True

if __name__ == '__main__':
    data = [1,2,3,3,2,1]
    head = make_linkedlist(data)
    s = Solution()
    ret = s.isPalindrome(head)
    print(ret)
            