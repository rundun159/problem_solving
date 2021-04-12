# Definition for a binary tree node.
from collections import defaultdict, deque
class QNode:
    def __init__(self, node, h):
        self.node = node
        self.height = h

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TH:
    def bfs(self, root):
        if root == None:
            return []
        q = deque()
        dict = defaultdict(list)
        q.append(QNode(root,0))
        total_h = 0
        while q:
            front = q.popleft()
            now_h = front.height
            dict[now_h].append(front.node.val)
            if front.node.left:
                q.append(QNode(front.node.left,now_h+1))
            if front.node.right:
                q.append(QNode(front.node.right,now_h+1))
            del front
            total_h = max(total_h, now_h)
        ret = []
        # print(dict)
        for i in range(total_h+1):
            ret.append(dict[i])
        return ret
class Solution:
    def levelOrder(self, root: TreeNode):
        th = TH()
        return th.bfs(root)

# n_15 = TreeNode(15)
# # n_7 = TreeNode(7)
# # n_20 = TreeNode(20,n_15,n_7)
# # n_9 = TreeNode(9)
# # n_3 = TreeNode(3,n_9,n_20)
# sol = Solution()
# print(sol.levelOrder(n_15))