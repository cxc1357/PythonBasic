class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self,head,target):
        cur = head
        while cur:
            if cur.val == target:
                # 将要删除节点的值改为下一个节点，再指向下下个节点
                # 适用于删除非尾部节点
                cur.val = cur.next.val
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head

if __name__ == "__main__":
    original_list = [1,7,3,6,5,8]
    target = 5

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
    res = so.deleteNode(head,target=target)

    while res:
        print(res.val)
        res = res.next
