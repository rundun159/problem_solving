from collections import deque
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class q_node:
    def __init__(self, node, h):
        self.node = node
        self.h = h
class Solution(object):
    def rightSideView(self, root):
        ret = []
        q = deque()
        q.append(q_node(root,0))
        now_h = -1
        last_right_val = None
        while len(q) != 0:
            now_qnode = q.popleft()
            if now_qnode.node == None:
                continue
            if now_h != now_qnode.h and now_qnode.h != 0:
                ret.append(last_right_val)
                now_h = now_qnode.h
            last_right_val = now_qnode.node.val
            q.append(q_node(now_qnode.node.left, now_qnode.h+1))
            q.append(q_node(now_qnode.node.right ,now_qnode.h+1))
            del now_qnode
        if last_right_val != None:
            ret.append(last_right_val)
        return ret
#
# node_5 = TreeNode(5)
# node_4 = TreeNode(4)
# node_2 = TreeNode(2,None, node_5)
# node_3 = TreeNode(3,None, node_4)
# root = TreeNode(1, node_2, node_3)