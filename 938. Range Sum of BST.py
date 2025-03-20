from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        summed_val = 0

        # if root belongs to inclusive range [low, high]
        if low <= root.val <= high:
            summed_val += root.val

        if root.val > low and root.val > high:
            # go left
            summed_val += self.rangeSumBST(root.left, low, high)
        elif root.val < low and root.val < high:
            # go right
            summed_val += self.rangeSumBST(root.right, low, high)
        else:
            summed_val += self.rangeSumBST(root.left, low, high)
            summed_val += self.rangeSumBST(root.right, low, high)

        return summed_val
