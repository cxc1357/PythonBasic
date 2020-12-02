# day23：递归两两交换链表节点
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    # 递归调用函数，将问题拆解为相同的小规模子问题
    def swapPairs(self,head):
        if head is None or head.next is None:
            return head
        tmp = head.next
        r = self.swapPairs(tmp.next)
        tmp.next = head
        head.next = r
        return tmp

if __name__ == "__main__":
    s = [1,2,3,4]

    head = ListNode(None)
    cur = head
    for i in s:
        newNode = ListNode(i)
        cur.next = newNode
        cur = cur.next
    head = head.next        
        
    so = Solution()
    result = so.swapPairs(head)
    tmp = result
    while tmp:
        print(tmp.val)
        tmp = tmp.next 
    