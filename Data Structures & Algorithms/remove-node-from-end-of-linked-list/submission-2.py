# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #first we need to find the first value before our target
        dummy = ListNode(0, head)

        slow = dummy
        fast = dummy

        for i in range(n):
            fast = fast.next
        
        
        while fast and fast.next:
            slow = slow.next  # slow should now be at the point before the target
            fast = fast.next
        
        slow.next = slow.next.next

        return dummy.next
        