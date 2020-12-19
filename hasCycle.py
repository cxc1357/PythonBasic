# day40：判断链表是否有环
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self,head):
        s = set()
        tmp = head
        while tmp:
            if tmp in s:
                return True
            s.add(tmp)
            tmp = tmp.next
        return False

if __name__ == "__main__":
    head = ListNode(None)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = head.next.next

    so = Solution()
    res = so.hasCycle(head)
    print(res)
    

