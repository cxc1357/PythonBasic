# day14:反转链表
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self,head):
        preNode = None
        curNode = head
        while curNode:
            next = curNode.next
            curNode.next = preNode
            preNode = curNode
            curNode = next
        return preNode

if __name__ == "__main__":
    original_list = [1,7,3,6,5,8]

    # 哑节点创建链表
    head = ListNode(None)
    tmp = head
    for i in original_list:
        newNode = ListNode(i)
        # 迭代
        tmp.next = newNode
        tmp = newNode
    head = head.next

    so = Solution()
    res = so.reverseList(head)
    print(res.val)
    print(res.next.val)