import sys
import math
sys.setrecursionlimit(100000)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def pre(node, low = -math.inf, high = math.inf):
            if not node:
                return True
            if node.val <= low or node.val >= high:
                return False
            return (pre(node.left,low,node.val) and pre(node.right, node.val, high))
        return pre(root)