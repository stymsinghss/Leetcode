from typing import  Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_middle, middle_node = self.middle(head)

        if not prev_middle:
            return None
        else:
            prev_middle.next = middle_node.next
        return head

    def middle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        t,h = head, head
        prev = None
        while h and h.next:
            prev = t
            t, h = t.next, h.next.next
        return (prev, t)