# day47:求二叉树最小深度
# 最小深度指从根节点到最近叶子节点的最短路径上的节点数量
# 叶子节点指没有子节点的节点
# 注意递归终止条件，容易漏掉左/右子树为空的情况
# 比如，只有根节点和左子节点，深度为2而不是1
from listToBinarytree import listToBinarytree

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def minDepth(self,root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        
        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)

        return 1 + min(self.minDepth(root.left),self.minDepth(root.right))

if __name__ == "__main__":
    so = Solution()
    #binaryTree = listToBinarytree([3,9,20,None,None,15,7])
    binaryTree = listToBinarytree([1,2,3,4,5,6,7])
    res = so.minDepth(binaryTree)
    print(res)