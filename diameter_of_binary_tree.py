# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # Stack for post-order traversal
        stack = [(root, False)]
        heights = {}
        diameter = 0
        
        while stack:
            node, visited = stack.pop()
            
            if visited:
                # Post-order: process node after children
                left_height = heights.get(node.left, 0)
                right_height = heights.get(node.right, 0)
                
                # Update diameter
                diameter = max(diameter, left_height + right_height)
                
                # Store height of this node
                heights[node] = 1 + max(left_height, right_height)
            else:
                # Pre-order: push node then children
                stack.append((node, True))
                if node.right:
                    stack.append((node.right, False))
                if node.left:
                    stack.append((node.left, False))
        
        return diameter