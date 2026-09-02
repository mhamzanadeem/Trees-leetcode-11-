# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Hash map to store tree hashes
        self.hash_map = {}
        # Flag to indicate if subRoot was found
        self.found = False
        
        # Get hash of subRoot
        sub_hash = self._hash_tree(subRoot)
        
        # Traverse root and compare hashes
        self._traverse_and_compare(root, sub_hash)
        
        return self.found
    
    def _hash_tree(self, node: Optional[TreeNode]) -> str:
        """Generate a unique hash for each tree using post-order traversal"""
        if not node:
            return "#"  # null node marker
        
        # Generate hash for left and right subtrees
        left_hash = self._hash_tree(node.left)
        right_hash = self._hash_tree(node.right)
        
        # Create unique hash for this node
        # Using string concatenation to ensure uniqueness
        # Including the node value and hashes of children
        node_hash = f"({node.val}|{left_hash}|{right_hash})"
        
        return node_hash
    
    def _traverse_and_compare(self, node: Optional[TreeNode], target_hash: str) -> str:
        """Traverse tree and compare each subtree hash with target"""
        if not node:
            return "#"
        
        # Get hash of left and right subtrees
        left_hash = self._traverse_and_compare(node.left, target_hash)
        right_hash = self._traverse_and_compare(node.right, target_hash)
        
        # Create hash for current subtree
        current_hash = f"({node.val}|{left_hash}|{right_hash})"
        
        # Check if this subtree matches the target
        if current_hash == target_hash:
            self.found = True
        
        return current_hash