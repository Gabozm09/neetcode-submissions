# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_term = head
        prev = None

        while current_term:
            temp = current_term.next
            current_term.next = prev
            prev = current_term
            current_term = temp
        return prev