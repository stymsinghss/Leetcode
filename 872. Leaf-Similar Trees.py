from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True

        if not root1 or not root2:
            return False

        leaves_root1, leaves_root2 = [], []
        self.getLeaves(root1, leaves_root1)
        self.getLeaves(root2, leaves_root2)

        return leaves_root1 == leaves_root2

    def getLeaves(self, root, leaves):
        if not root:
            return None

        if not root.left and not root.right:
            leaves.append(root.val)

        self.getLeaves(root.left, leaves)
        self.getLeaves(root.right, leaves)