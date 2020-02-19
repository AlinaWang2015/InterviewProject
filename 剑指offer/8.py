# 题目描述
# 给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
# 注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。

# 这道题意即：给定一个节点，按照中序遍历（左根右）的方式求该节点的下一个节点。有三种情况：
# 1. 给定的节点为空——返回空；例如：A
# 2. 给定的节点有右子树——沿着该右子树，返回右子树的第一个左叶子节点；例如：E节点的下一个节点是M
# 3. 给定的节点没有右子树——如果位于某个节点的左子树中，则上溯直至找到该节点；否则就返回空。
# 【因为按照中序遍历“左中右”的遍历方式，当该节点没有右子树时，要么遍历完毕，
# 下一个节点为空；要么某个子树的左子树遍历完毕，下一个节点是子树的根节点】

class Solution:
    def GetNext(self, pNode):
        if not pNode:
            return
        if not pNode.right:
            return self.getHead(pNode)
        return self.getRightNode(pNode.right)

    def getHead(self, pNode):
        while pNode.next:
            if pNode.next.right == pNode:
                pNode = pNode.next
            elif pNode.next.left == pNode:
                return pNode.next
        return None

    def getRightNode(self, pNode):
        while pNode.left:
            pNode = pNode.left
        return pNode