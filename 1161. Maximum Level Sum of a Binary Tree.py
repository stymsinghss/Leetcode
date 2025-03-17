from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1

        q = deque([root])
        level_sum = []
        level = 1
        while q:
            cur_level_sum = 0
            for i in range(len(q)):
                node = q.popleft()
                cur_level_sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            level_sum.append((level, cur_level_sum))
            level += 1
        levels = sorted(level_sum, key = lambda x:x[1], reverse = True)
        return levels[0][0]