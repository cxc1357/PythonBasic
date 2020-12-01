class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:    
    def getiNode(self,head,n,i):
        if i < 0 or i > n:
            raise IndexError
        cur = head
        # _是占位符，代表each
        for _ in range(i):
            cur = cur.next
        return cur

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
    res = so.getiNode(head,6,4)
    print(res.val)
       