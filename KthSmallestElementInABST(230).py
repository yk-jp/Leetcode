# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = [0, 0]
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res[1] += 1
            if res[1] == k:
                res[0] = root.val
                return
            inorder(root.right)
    
        inorder(root)
        return res[0]