from collections import defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class TH:
    def ret_root(self, preorder, inorder):
        if not preorder:
            return None
        root_val = preorder[0]
        root = TreeNode(root_val)
        if len(preorder) == 1:
            return root
        # print(root_val, preorder, inorder)
        for idx, val in enumerate(inorder):
            if root_val == val:
                inorder_root_idx = idx
                break
        # print("inorder root idx : " ,inorder_root_idx)
        dict = defaultdict(bool)
        for i in inorder[:inorder_root_idx]:
            dict[i] = True
        found = False
        for idx, val in enumerate(preorder[1:]):
            # print(dict[val], val, idx)
            if not dict[val]:
                right_subtree_root_idx = idx
                found=True
                break
        if found:
            right_subtree_root_idx += 1
        else:
            right_subtree_root_idx = len(preorder)
        # print("right_subtree_root_idx : ",right_subtree_root_idx)
        left = self.ret_root( preorder[1 : right_subtree_root_idx], inorder[ : inorder_root_idx])
        right = self.ret_root( preorder[right_subtree_root_idx : ], inorder[inorder_root_idx+1 : ])
        root.left = left
        root.right = right
        return root
class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        th = TH()
        return th.ret_root(preorder,inorder)

# sol = Solution()
# root = sol.buildTree([3,9,20,15,7],[9,3,15,20,7])
# root