class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import math
import sys
sys.setrecursionlimit(10000000)

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.stack = []
        self.p_stack = []
        self.p_found = False
        self.q_stack = []
        self.q_found = False
        self.p = p.val
        self.q = q.val
        self.p_len = 0
        self.q_len = 0


        self.stack.append(root)
        self.dfs(root)
        self.stack.pop()

        LCA= None

        if self.p_len <= self.q_len:
            p_short = True
            q_short = False
        else:
            p_short = False
            q_short = True
        short = min(len(self.p_stack),len(self.q_stack))
        prev = None
        # print(self.p_stack)
        # print(self.q_stack)
        for i in range(short):
            if self.p_stack[i] != self.q_stack[i]:
                return prev
            else:
                prev = self.p_stack[i]
        if p_short:
            return self.p_stack[-1]
        if q_short:
            return self.q_stack[-1]

    def dfs(self,node):
        if not node:
            return
        if node.val == self.p:
            self.p_found = True
            self.p_stack = [x for x in self.stack]
            self.p_len = len(self.p_stack)
        if node.val == self.q:
            self.q_found = True
            self.q_stack = [x for x in self.stack]
            self.q_len = len(self.q_stack)
        if self.p_found and self.q_found:
            return
        for n in [node.left, node.right]:
            if n:
                self.stack.append(n)
                self.dfs(n)
                self.stack.pop()
        return