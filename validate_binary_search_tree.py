# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, min_val, max_val):
            if not node:
                return True
            
            # Current node's value must be within the valid range
            if node.val <= min_val or node.val >= max_val:
                return False
            
            # For left subtree: values must be < node.val (max becomes node.val)
            # For right subtree: values must be > node.val (min becomes node.val)
            return (validate(node.left, min_val, node.val) and 
                    validate(node.right, node.val, max_val))
        
        # Use None for infinity since values can be very large/small
        return validate(root, float('-inf'), float('inf'))