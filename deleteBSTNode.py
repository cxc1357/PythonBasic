# day60:删除二叉搜索树某节点
# 给定root和key，删除key对应的节点，保证二叉搜索树性质不变
# 时间复杂度为O(h)，h为树高度
# 1.key小于root，在左子树中查找
# 2.key大于root，在右子树中查找
# 3.key等于root，分4种情况
#   1) root无子树，摘除root，返回None
#   2) root仅有左子树，删除root，返回root.left
#   3) root仅有右子树，删除root，返回node.right
#   4) root有左右子树，删除root，以右子树的最小节点[代替]被删除的节点
# 这里的[代替]指值代替，不破坏原先的左右节点关系

class Solution:
    def deleteNode(self,root,key):
        return self.__delNodei(root,key)

    def __findMinNode(self,nodei):
        if not nodei.left:
            return nodei
        while nodei.left:
            nodei = nodei.left
        return nodei

    def __delNodei(self,nodei,key):
        if not nodei:
            return None
        # 情况1:待删除节点在左子树
        if key < nodei.val:
            nodei.left = self.__delNodei(nodei.left,key)
        # 情况2:待删除节点在右子树
        elif nodei.val<key:
            nodei.right = self.__delNodei(nodei.right,key)
        # 情况3:当前节点为待删除节点
        else:
            # 情况3.1:当前节点没有子树i
            if not nodei.left and nodei.right:
                return None
            # 情况3.2:当前节点没有右子树
            if not nodei.right:
                return nodei.left
            # 情况3.3:当前节点没有左子树i
            if not nodei.left:
                return nodei.right
            # 情况3.4:当前节点有左右子树
            # 找右子树最小节点
            minNodei = self.__findMinNode(nodei.right)
            nodei.val = minNodei.val
            # 删除minNodei，同时返回nodei.right的引用，并赋值给nodei.right
            nodei.right = self.__delNodei(nodei.right,minNodei.val)
        return nodei

## 这个写法的命名更清晰些
# class Solution(object):
#     def deleteNode(self, root, key):
#         """
#         :type root: TreeNode
#         :type key: int
#         :rtype: TreeNode
#         """
#         if not root:
#             return None
#         #到左子树里搜索
#         if root.val > key:
#             root.left = self.deleteNode(root.left, key)
#         #到右子树里搜索
#         elif root.val < key:
#             root.right = self.deleteNode(root.right, key)
#         else:
#         	# 存在的子树代替根节点
#             if not root.left or not root.right:
#                 root = root.left if root.left else root.right
#             else:
#                 temp = root.right
#                 # 找到右子树的最小（最左）节点
#                 while temp.left: 
#                     temp = temp.left
#                 root.val = temp.val
#                 # 继续在右子树里递归
#                 root.right = self.deleteNode(root.right, temp.val)
            
#         return root