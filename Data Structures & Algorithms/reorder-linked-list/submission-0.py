# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #div the list into two equal halves
        #Use fast and slow pointers
        l = head
        r = head
        while r and r.next:
            l=l.next
            r=r.next.next
        r= l.next
        l.next = None

        #reverse the second part
        prev = None
        cur = r
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        r = prev

        #join the list
        first = head
        second = r

        while second:
            t1 = first.next
            t2=second.next

            first.next = second
            second.next = t1

            first = t1
            second = t2
        