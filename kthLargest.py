# day58：二叉树搜索第k大节点
# 中序遍历即可得到结果，但不需要全部遍历，右子树遍历完没找到再去左子树找

from listToBinarytree import listToBinarytree

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthLargest(self,root,k):
        self.count = k
        self.found = False
        
        # 遍历子树
        def travel(node):
            if not node or self.found:
                return
            # 遍历右子树
            travel(node.right)
            # 找第k大
            self.count -= 1
            # 找到了
            if self.count == 0:
                self.result = node.val
                self.found = True
                return
            # 右子树没找到，遍历左子树
            if not self.found:
                travel(node.left)
        travel(root)

        return self.result

if __name__ == "__main__":
    so = Solution()
    binaryTree = listToBinarytree([2,1,3])
    # binaryTree = listToBinarytree([1,2,3,4,5,6,7])
    res = so.kthLargest(binaryTree,2)
    print(res)