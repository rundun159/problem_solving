# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        if not root:
            return []
        self.flatten = []
        self.flatten_f(root)
        for idx, n in enumerate(self.flatten[:-1]):
            n.left = None
            n.right = self.flatten[idx+1]
        self.flatten[-1].left = None
        self.flatten[-1].right = None
    def flatten_f(self, node):
        if not node:
            return
        self.flatten.append(node)
        self.flatten_f(node.left)
        self.flatten_f(node.right)
        return