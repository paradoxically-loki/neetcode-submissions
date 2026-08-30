# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        leftPrev, curr = dummy, head

        for _ in range(left-1):
            leftPrev, curr = curr, curr.next

        prev = None
        for _ in range(right - left + 1):
            tempNext = curr.next
            curr.next = prev
            prev = curr
            curr = tempNext

        leftPrev.next.next = curr #connect from the end of the reversed list
        leftPrev.next = prev # connects the front of the reversed list

        return dummy.next
        