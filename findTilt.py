# day52:二叉树坡度
# 树节点的坡度为该节点左子树的节点之和和右子树节点之和的差的绝对值，空节点坡度为零，树的坡度为所有节点坡度之和
from listToBinarytree import listToBinarytree

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findTilt(self,root):
        self.tilt = 0
        def treeSum(root):
            if not root:
                return 0
            leftSum = treeSum(root.left)
            rightSum = treeSum(root.right)
            self.tilt += abs(leftSum-rightSum)
            return leftSum + rightSum + root.val
        treeSum(root)
        return self.tilt

if __name__ == "__main__":
    so = Solution()
    binaryTree = listToBinarytree([1,2,3,5,2])
    res = so.findTilt(binaryTree)
    print(res)



