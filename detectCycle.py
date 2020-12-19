# day41：找到有环链表的入口点
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self,head):
        if not head or not head.next:
            return None
        slow,fast = head,head
        while True:
            if not fast or not fast.next:
                return None
            # 慢指针一次一步，快指针一次两步
            slow = slow.next
            fast = fast.next.next
            # 重合时说明有环
            if slow == fast:
                break
        slow = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return slow

if __name__ == "__main__":
    head = ListNode(None)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = head.next.next

    so = Solution()
    res = so.detectCycle(head)
    print(res.val)