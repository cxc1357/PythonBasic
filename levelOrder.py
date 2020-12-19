# day53:二叉树层序遍历
# 按照根-左-右顺序入队

from listToBinarytree import listToBinarytree
from collections import deque

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self,root):
        if not root:
            return []
        search_queue = deque()
        search_queue.append(root)
        result = []

        # visited 记录每层结果
        while search_queue:
            visited = []
            for i in range(len(search_queue)):
                node = search_queue.popleft()
                visited.append(node.val)
                if node.left:
                    search_queue.append(node.left)
                if node.right:
                    search_queue.append(node.right)
            result.append(visited)
        
        return result

if __name__ == "__main__":
    so = Solution()
    #binaryTree = listToBinarytree([3,9,20,None,None,15,7])
    binaryTree = listToBinarytree([1,2,3,4,5,6,7])
    res = so.levelOrder(binaryTree)
    print(res)