# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ite = root
        self.dfs(ite)
        
        return root
    
    def dfs(self, curr):
        if not curr:
            return
        
        tmp = curr.left
        curr.left = curr.right
        curr.right = tmp
        
        self.dfs(curr.left)
        self.dfs(curr.right)