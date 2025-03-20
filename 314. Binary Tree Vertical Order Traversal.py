from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        mapper = {}

        q = deque([(root, 0)])
        while q:
            for i in range(len(q)):
                node, level = q.popleft()
                if level in mapper:
                    mapper[level].append(node.val)
                else:
                    mapper[level] = [node.val]

                if node.left:
                    q.append((node.left, level-1))
                if node.right:
                    q.append((node.right, level+1))

        # sort based on key
        sorted_dict = dict(sorted(mapper.items(), key= lambda x:x[0]))
        return list(sorted_dict.values())
        