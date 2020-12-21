# day59：二叉搜索树两个节点的最近公共父节点（一个节点可以是自己的祖先）

from listToBinarytree import listToBinarytree

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self,root,p,q):
        if root.val < min(p.val,q.val):
            return self.lowestCommonAncestor(root.right,p,q)
        elif max(p.val,q.val) < root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        else:
            return root

if __name__ == "__main__":
    so = Solution()
    binaryTree = listToBinarytree([2,1,3])
    # binaryTree = listToBinarytree([1,2,3,4,5,6,7])
    res = so.lowestCommonAncestor(binaryTree,binaryTree.left,binaryTree.right)
    print(res.val)