# day46:列表转为二叉树
#   3
#  / \
# 9  20
#   /  \
#  15   7

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def listToBinarytree(nums):
    def level(index):
        if index >= len(nums) or nums[index] is None:
            return None
        root = TreeNode(nums[index])
        root.left = level(2*index + 1)
        root.right = level(2*index + 2)
        return root
    return level(0)

binaryTree = listToBinarytree([3,9,20,None,None,15,7])

