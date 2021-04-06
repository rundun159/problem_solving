# Definition for a binary tree node.
import sys
import math
sys.setrecursionlimit(100000)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        math.inf

class TH:
    def __init__(self,root):
        self.root = root
    def ret_min_max(self, node):
        ret = [None, None]
        cond = True
        if node.left == None:
            ret[0] = node.val
        else:
            left_ret, cond = self.ret_min_max(node.left)
            if not cond:
                return [None, None], False
            elif node.val > left_ret[1]:
                ret[0] = left_ret[0]
            else:
                return [None, None], False
        if node.right == None:
            ret[1] = node.val
        else:
            right_ret, cond = self.ret_min_max(node.right)
            if not cond:
                return [None, None], False
            elif node.val < right_ret[0]:
                ret[1] = right_ret[1]
            else:
                return [None, None], False
        return ret, True
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        th = TH(root)
        ret_list, ret_bool =  th.ret_min_max(root)
        return ret_bool