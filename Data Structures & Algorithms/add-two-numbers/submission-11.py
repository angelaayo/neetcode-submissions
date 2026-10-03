# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #traverse through both lists summing up and keeping track of
        # a carry if any
        dummy = node = ListNode()
        carry = 0
        while l1 or l2:
            val = 0
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            sum = carry + val1 + val2
            val = sum % 10
            carry = sum//10
            newNode = ListNode(val)
            node.next = newNode
            node = node.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # in the event we still have a carry
        if carry > 0:
            newNode = ListNode(carry)
            node.next = newNode
        return dummy.next
            

        