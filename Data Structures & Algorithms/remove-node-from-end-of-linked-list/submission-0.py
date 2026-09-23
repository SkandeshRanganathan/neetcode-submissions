# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp1 = head
        temp2 = head
        for _ in range(n):
            temp1 = temp1.next
        if temp1 is None:
            return head.next
        while temp1.next:
            temp1 = temp1.next
            temp2 = temp2.next
        temp2.next = temp2.next.next
        return head