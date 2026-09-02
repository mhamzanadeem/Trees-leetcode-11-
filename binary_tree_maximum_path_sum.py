# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Initialize with minimum possible value since nodes can be negative
        self.max_sum = float('-inf')
        
        def max_gain(node):
            if not node:
                return 0
            
            # Maximum sum from left and right subtrees
            # If negative, we can choose to not take that path (0)
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            
            # Maximum path sum that passes through this node
            # This is the sum of: node.val + left_gain + right_gain
            current_max = node.val + left_gain + right_gain
            
            # Update global maximum
            self.max_sum = max(self.max_sum, current_max)
            
            # Return the maximum sum starting from this node going down
            # We can only take one branch (left or right), whichever gives more
            return node.val + max(left_gain, right_gain)
        
        max_gain(root)
        return self.max_sum