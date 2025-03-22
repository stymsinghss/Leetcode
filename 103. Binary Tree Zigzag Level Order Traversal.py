from typing import Optional,List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        levels = []
        q = deque([root])

        direction = True
        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()

                if direction:
                    level.append(node.val)
                else:
                    level.insert(0, node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            levels.append(level)
            direction = not direction
        return levels