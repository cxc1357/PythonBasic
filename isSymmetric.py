# day49:二叉树是否镜像对称
from listToBinarytree import listToBinarytree

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self,root):
        # 空树
        if not root:
            return True
        # 对根节点的左右子节点进行递归判断
        def sub(left,right):
            # 没有左右子树
            if not left and not right:
                return True
            # 左右子树有一个为空
            if not left or not right:
                return False
            # 左右子树根节点值相等，且对称位置叶子节点值相等
            # 需要保证，遍历时走的方向是对称的，如左子树往右，同时右子树往左
            return left.val == right.val and sub(left.left,right.right) and sub(left.right,right.left)
        return sub(root.left,root.right)

if __name__ == "__main__":
    so = Solution()
    binaryTree = listToBinarytree([1,2,2,3,4,4,3])
    res = so.isSymmetric(binaryTree)
    print(res)
