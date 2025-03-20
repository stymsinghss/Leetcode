from typing import List, Optional
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Pair:
    def __init__(self, ll_val,ll):
        self.ll_val = ll_val
        self.ll = ll

    def __lt__(self, other):
        return self.ll_val < other.ll_val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for ll in lists:
            if ll:
                heapq.heappush(heap, Pair(ll.val, ll))

        head = ListNode(-1)
        dummy = head

        while heap:
            pair = heapq.heappop(heap)
            val, ll = pair.ll_val, pair.ll
            dummy.next = ListNode(val)
            dummy = dummy.next

            if ll.next:
                heapq.heappush(heap, Pair(ll.next.val, ll.next))

        return head.next
