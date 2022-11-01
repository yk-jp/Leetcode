# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
     
        def in_order(root, arr):
            if not root:
                return arr
            in_order(root.left, arr)
            arr.append(root.val)
            in_order(root.right, arr)
            
            return arr
            
        r1_arr = in_order(root1, [])
        r2_arr = in_order(root2, [])

        res = []
        
        i = 0
        j = 0
        
        while i < len(r1_arr) and j < len(r2_arr):
            
            if r1_arr[i] <= r2_arr[j]:
                res.append(r1_arr[i])
                i += 1
            else:
                res.append(r2_arr[j])
                j += 1
        
        if i >= len(r1_arr):
            res += r2_arr[j:]
        else:
            res += r1_arr[i:]
                
        return res