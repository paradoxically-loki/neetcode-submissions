# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        curr = l1
        s1 = ""
        while curr:
            s1 += str(curr.val)
            curr = curr.next

        curr = l2
        s2 = ""
        while curr:
            s2 += str(curr.val)
            curr = curr.next

        out = int(s1[::-1]) + int(s2[::-1])
        out_str = str(out)[::-1]

        dummy = ListNode()
        tail = dummy
        for ch in out_str:
            tail.next = ListNode(int(ch))
            tail = tail.next
        
        return dummy.next
        