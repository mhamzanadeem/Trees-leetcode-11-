# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            if not node:
                return 0
            
            # Check if current node is good
            # It's good if its value is >= max value seen so far
            is_good = 1 if node.val >= max_val else 0
            
            # Update max value for children
            new_max = max(max_val, node.val)
            
            # Recursively count good nodes in left and right subtrees
            left_count = dfs(node.left, new_max)
            right_count = dfs(node.right, new_max)
            
            return is_good + left_count + right_count
        
        # Start with root's value as the initial maximum
        return dfs(root, root.val)