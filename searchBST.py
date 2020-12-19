# day57：二叉搜索树查找
# 可能有重复元素
from listToBinarytree import listToBinarytree

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

# 封装一层的意义是包含返回数组r
def searchNode(root,target):
    r = []
    def search(root,target):
        if not root:
            return r
        if target == root.val:
            r.append(target)
            search(root.left,target)
            search(root.right,target)
        elif target < root.val:
            search(root.left,target)
        else:
            search(root.right,target)
        return r
    return search(root,target)

BST = listToBinarytree([2,1,3])
res = searchNode(BST,2)
print(res)
