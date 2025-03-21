from collections import deque
from typing import Dict, List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findParents(self, root: TreeNode, pmap: Dict[TreeNode, TreeNode]) -> None:
        if not root:
            return

        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                    pmap[node.left] = node
                if node.right:
                    q.append(node.right)
                    pmap[node.right] = node

    def findStartNode(self, root: Optional[TreeNode], start: int) -> TreeNode:
        if not root:
            return None

        if root.val == start:
            return root

        return self.findStartNode(root.left, start) or self.findStartNode(root.right, start)

    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        pmap, visited = dict(), set()
        self.findParents(root, pmap)

        start_node = self.findStartNode(root, start)
        q = deque([start_node])
        visited.add(start_node)
        time = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()

                if node.left and node.left not in visited:
                    q.append(node.left)
                    visited.add(node.left)
                if node.right and node.right not in visited:
                    q.append(node.right)
                    visited.add(node.right)
                if pmap.get(node) is not None and pmap.get(node) not in visited:
                    q.append(pmap.get(node))
                    visited.add(pmap.get(node))
            time += 1

        return time - 1
