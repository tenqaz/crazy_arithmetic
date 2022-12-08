#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File: dropball.py
@Time: 2022/12/08 17:55:49
@Author: Jim
@Contact: zhengwenfeng37@gmail.com
@Desc: 

    小球下落问题

    有一棵二叉树,最大深度为D,且所有叶子的深度都相同。所有结点从上到下,从左到右编号为1,2,3,…,2D-1。

在结点1处放一个小球,它会往下落。每个结点上都有一个开关,初始全部关闭,当每次有小球落到一个开关上时,它的状态都会改变。当小球到达一个内部结点时,如果该结点上的开关关闭,则往左走,否则往右走,直到走到叶子结点。如图所示。

一些小球从结点1处依次下落,最后一个小球将会落到哪里?输入叶子的深度D和和小球个数I,输出第I个小球最后所在叶子的编号。

输入:4 2

输出:12

输入:8 128

输出:255 
'''

def main(deep, num):
    """ 记录所有节点的状态。遍历，获取最后一次遍历所在节点的值。

        deep: 二叉树的深度
        num: 小球的数量
    """

    nodes = [False for i in range(1<<deep)]

    cur_index = 1
    MAX = (1<<deep)-1
    for i in range(num):
        cur_index = 1
        while True:

            if nodes[cur_index]:
                nodes[cur_index] = not nodes[cur_index]
                cur_index = cur_index*2+1
                
            else:
                nodes[cur_index] = not nodes[cur_index]
                cur_index = cur_index*2
                

            if cur_index > MAX:
                break
            
    print(cur_index/2)

def main2(deep, num):
    """ 找规律
        deep: 二叉树的深度
        num: 小球的数量

        小球数量双数往右走，单数往左走。
    """
    
    ret = 1
    for i in range(deep-1):

        if num % 2 == 1:
            ret *= 2
            num = (num + 1) / 2
        else:
            ret = ret*2 + 1
            num /= 2
    
    print(ret)




if __name__ == "__main__":
    main(4, 2)
    # main(8, 128)