# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return root

        if not p and not q:
            return None
        if not p or not q:
            return root

        if root.val == p.val or root.val == q.val:
            return root

        left_search = self.lowestCommonAncestor(root.left, p, q)
        right_search = self.lowestCommonAncestor(root.right, p, q)

        if not left_search:
            return right_search
        elif not right_search:
            return left_search
        else:
            return root