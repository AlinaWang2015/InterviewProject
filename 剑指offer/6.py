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


# 真正解决思路
# 其实，在这链表操作中，从头到尾打印一遍只需要一个简单的遍历便可以做到。
# 然而在这里，遍历的顺序是从头到尾，而打印的顺序是从尾到头，这就是典型的 “先进后出”，
# 因此，可采用 栈 或着 递归 实现。

class LinkedListNode(object):
    def __init__(self,next=None,value=None):
        self.next = next
        self.value = value
# 采用一下方式简单的创建一个链表
# 由于链表新插入的节点在表头，因此，实际上链表中的顺序，与插入列表的顺序是反过来
pHead = LinkedListNode()
myList = [1,2,3,4,5,6,7,8,9]
for i in range(len(myList)):
    pHead = LinkedListNode(pHead,myList[i])

# 以上新建了链表，其遍历顺序为：9 8 7 6 5 4 3 2 1



# 栈
def printLinkedListReversingly_stack(pHead):
    if pHead.value==None:
       return False
    tempList = []
    while pHead.value:
        tempList.append(pHead.value)
        pHead = pHead.next
    while tempList:
        print(tempList.pop())


# 递归
def printLinkedList(pHead):
    if pHead.value==None:
        return False
    printLinkedList(pHead.next)
    print(pHead.value)

