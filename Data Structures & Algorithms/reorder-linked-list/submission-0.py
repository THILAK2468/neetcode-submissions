# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
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
            temp1 = l1.next
            temp2 = l2.next

            l1.next = l2
            l2.next = temp1

            l1=temp1
            l2 = temp2

