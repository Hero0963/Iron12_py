from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# solution1
class Solution1:
    """
    N=number of nodes
    time: O(N)
    space: O(1)
    """

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


# solution2
class Solution2:
    """
    N=number of nodes
    time: O(N)
    space: O(1)
    """

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        return root
