# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #find the length N of the LL
        length = 0
        p = head
        while p:
            length+=1
            p=p.next
        p=head
        #remove (N-n)th node from the list
        for i in range(length - n-1):
            p=p.next
        if length == n:
            return head.next
        else:
            p.next = p.next.next
        return head