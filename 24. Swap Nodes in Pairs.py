from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        1. what if we don't have head
        2. What if we don't have enough nodes for swapping

        If we have nodes
        1. get two nodes (consecutive)
        2. Swap them
        3. Recursively do the same for other nodes of the LL
        """

        if not head:
            return None

        if not head.next:
            return head

        first_node = head
        second_node = head.next
        rem_nodes = second_node.next

        second_node.next = first_node
        first_node.next = self.swapPairs(rem_nodes)

        return second_node