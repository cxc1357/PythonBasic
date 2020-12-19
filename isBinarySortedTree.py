# day56：判断是否二叉搜索树
# 定义：对于树中任一节点r，左/右子树中的节点均不大/小于r

from listToBinarytree import listToBinarytree

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    # 参数扩展
    def isBinarySortedTree(self,root):
        return self.isBST(root,float('-inf'),float('inf'))
    
    # 每个节点是其左子树的最大值，右子树的最小值
    def isBST(self,root,lower,upper):
        # 如果子树为空则不用比较
        if root == None:
            return True
        if lower>=root.val or upper<=root.val:
            return False
        return self.isBST(root.left,lower,root.val) and self.isBST(root.right,root.val,upper)

if __name__ == "__main__":
    so = Solution()
    binaryTree = listToBinarytree([2,1,3])
    # binaryTree = listToBinarytree([1,2,3,4,5,6,7])
    res = so.isBinarySortedTree(binaryTree)
    print(res)