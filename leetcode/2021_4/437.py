# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        if not root:
            return 0
        stack = []
        self.target = targetSum
        self.ret = 0
        self.dfs(0, stack, root)
        return self.ret

    def dfs(self, stackSum, stack, node):
        next_sum = stackSum + node.val
        if next_sum == self.target:
            self.ret += 1
        now_sum = next_sum
        for s in stack:
            now_sum -= s
            if now_sum == self.target:
                self.ret += 1
        for next_node in [node.left, node.right]:
            if next_node:
                stack.append(node.val)
                self.dfs(next_sum, stack, next_node)
                stack.pop()
