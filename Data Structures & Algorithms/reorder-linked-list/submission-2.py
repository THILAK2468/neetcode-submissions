# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return 
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        l1=head
        l2= slow.next
        prev = None
        current = l2
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        l2=prev
        slow.next=None
        while l2:
            l1.next,l1 = l2,l1.next
            l2.next,l2 = l1,l2.next

