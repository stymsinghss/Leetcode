from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # TC -> O(n) where n is the number of nodes in the tree
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right_view = []
        if not root:
            return right_view

        q = deque([root])
        while q:
            right_node = None
            for i in range(len(q)):
                node = q.popleft()
                right_node = node

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            right_view.append(right_node.val)
        return right_view