# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # first reverse the second half of the list
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # so at this point slow is in the middle fast is at the end
        # we need to reverse 4 5 6
        temp = slow.next
        prev = None 
        while temp:
            afterVal = temp.next
            temp.next = prev
            prev = temp
            temp = afterVal
        slow.next = None # at this point slow should be attached to the reversed
        first = head
        second = prev
        while second:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next


        


        