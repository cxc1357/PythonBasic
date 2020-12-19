# day48：是否为单值二叉树
# 递归基情况
# 1.空树
# 2.1个节点
# 3.左子节点和根节点值不相等
# 4.右子节点和根节点值不相等

from listToBinarytree import listToBinarytree

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isUnivalTree(self,root):
        if not root:
            return True
        if not root.left and root.right:
            return True
        
        if root.left and root.left.val != root.val:
            return False
        if root.right and root.right.val != root.val:
            return False
        
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)

if __name__ == "__main__":
    so = Solution()
    binaryTree = listToBinarytree([1,1,1])
    res = so.isUnivalTree(binaryTree)
    print(res)

