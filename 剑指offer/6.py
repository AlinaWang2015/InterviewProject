# 题目描述
# 输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
#
# 理解
# 首先要理解链表的概念，链表是由一串串数字首尾相连组成的

# -*- coding:utf-8 -*-


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        list=[]
        while listNode:
            list.append(listNode.val)
            listNode = listNode.next
        return list[::-1]