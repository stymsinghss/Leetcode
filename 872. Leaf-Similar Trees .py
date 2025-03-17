from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaves_1, leaves_2 = [], []
        self.getLeaves(root1, leaves_1)
        self.getLeaves(root2, leaves_2)

        return leaves_1 == leaves_2

    def getLeaves(self, root: Optional[TreeNode], leaves: List[int]):
        if not root:
            return

        if not root.left and not root.right:
            leaves.append(root.val)
            return

        self.getLeaves(root.left, leaves[:])
        self.getLeaves(root.right, leaves[:])