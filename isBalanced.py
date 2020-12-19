# day54:是否平衡二叉树
# 定义：一个二叉树每个节点左右两个子树的高度差的绝对值不超过1

from listToBinarytree import listToBinarytree

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

# 相比于把getHeight写在isBalanced里更清晰，注意python类函数要加self
class Solution(object):
    
    def isBalanced(self,root):
        if not root:
            return True
        return abs(self.getHeight(root.left) - self.getHeight(root.right)) <=1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def getHeight(self,root):
        if not root:
            return True
        return 1 + max(self.getHeight(root.left),self.getHeight(root.right))

if __name__ == "__main__":
    so = Solution()
    binaryTree = listToBinarytree([1,2,2,3,3,None,None,4,4])
    # binaryTree = listToBinarytree([1,2,3,4,5,6,7])
    res = so.isBalanced(binaryTree)
    print(res)