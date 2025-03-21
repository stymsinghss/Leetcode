from typing import Dict, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
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

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        pmap, visited = dict(), set()
        self.findParents(root, pmap)

        q = deque([target])
        visited.add(target)
        dist = 0
        while q:
            if dist == k:
                break
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
            dist += 1

        dist_k_nodes = []
        while q:
            dist_k_nodes.append(q.popleft().val)

        return dist_k_nodes
