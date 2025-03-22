from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        paths = []
        self.getPaths(root, paths, [])
        summed_val = 0
        for path in paths:
            path_val = 0
            for p in path:
                path_val = path_val * 10 + p
            summed_val += path_val

        return summed_val

    def getPaths(self, root, path, temp) -> None:
        if not root:
            return []

        temp.append(root.val)
        if not root.left and not root.right:
            path.append(temp[:])
            return

        self.getPaths(root.left, path, temp[:])
        self.getPaths(root.right, path, temp[:])
