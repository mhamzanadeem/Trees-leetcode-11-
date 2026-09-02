# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import List, Optional

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            rightmost = None
            
            for i in range(level_size):
                node = queue.popleft()
                rightmost = node.val  # Keep updating with each node
                
                # Add children to queue (left then right)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # After processing the entire level, rightmost is the last node
            result.append(rightmost)
        
        return result