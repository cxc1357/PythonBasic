# day33：合并两个有序链表
class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class Solution:
    def createList(self,list):
        head = ListNode(None)
        temp = head
        for i in list:
            newNode = ListNode(i)
            temp.next = newNode
            temp = newNode
        head = head.next
        return head
    
    def printList(self,head):
        temp = head
        while temp != None:
            print(temp.val,end = ' ')
            temp = temp.next

    def mergeTwoLists(self,l1,l2):
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val <=l2.val:
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2

if __name__ == "__main__":
    so = Solution()

    list1=[1,3,5]
    head1 = so.createList(list1)

    list2=[2,4,6]
    head2 = so.createList(list2)
    
    result = so.mergeTwoLists(head1,head2)
    so.printList(result)

