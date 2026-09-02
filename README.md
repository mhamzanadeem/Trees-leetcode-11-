# Trees - LeetCode 11

## Problems

| # | Problem | Difficulty | Approach | File |
|---|---------|------------|----------|------|
| 543 | Diameter of Binary Tree | Easy | DFS | `diameter_of_binary_tree.py` |
| 572 | Subtree of Another Tree | Easy | DFS | `subtree_of_another_tree.py` |
| 236 | Lowest Common Ancestor of a BST | Medium | DFS | `lowest_common_ancestor_of_a_bst.py` |
| 102 | Binary Tree Level Order Traversal | Medium | BFS | `binary_tree_level_order_traversal.py` |
| 199 | Binary Tree Right Side View | Medium | BFS | `binary_tree_right_side_view.py` |
| 1448 | Count Good Nodes In Binary Tree | Medium | DFS | `count_good_nodes_in_binary_tree.py` |
| 98 | Validate Binary Search Tree | Medium | DFS | `validate_binary_search_tree.py` |
| 230 | Kth Smallest Element in a BST | Medium | DFS | `kth_smallest_element_in_a_bst.py` |
| 105 | Construct Binary Tree From Preorder and Inorder | Medium | DFS | `construct_binary_tree_from_preorder_and_inorder.py` |
| 124 | Binary Tree Maximum Path Sum | Hard | DFS | `binary_tree_maximum_path_sum.py` |
| 297 | Serialize and Deserialize Binary Tree | Hard | BFS/DFS | `serialize_and_deserialize_binary_tree.py` |

## DFS vs BFS Comparison

### Problems using DFS (Depth-First Search)

| Problem | Why DFS |
|---------|---------|
| Diameter of Binary Tree | Need to compute height of subtrees; recursion naturally tracks max depth |
| Subtree of Another Tree | Recursive comparison of node structures matches tree recursion |
| Lowest Common Ancestor of BST | Path-based search from root to target nodes |
| Count Good Nodes | Track max value along each root-to-leaf path |
| Validate BST | In-order or bounds-checking traversal |
| Kth Smallest Element in BST | In-order traversal gives sorted sequence |
| Construct Binary Tree | Recursive decomposition of subarrays |
| Binary Tree Maximum Path Sum | Compute max gain from each subtree upward |

### Problems using BFS (Breadth-First Search)

| Problem | Why BFS |
|---------|---------|
| Binary Tree Level Order Traversal | Level-by-level processing is natural with queue |
| Binary Tree Right Side View | Need rightmost node at each level |
| Serialize/Deserialize Binary Tree | Level-order traversal preserves structure for reconstruction |

### Decision Guide

- **Use DFS when**: processing paths, computing subtree properties, or recursion depth is manageable
- **Use BFS when**: processing level-by-level, or problem requires breadth information

---

## Key Concepts

### Why In-Order Traversal of BST Gives Sorted Order

In a BST, for any node:
- All left subtree values < node value
- All right subtree values > node value

In-order traversal visits: Left → Node → Right

This means:
1. Visit all smaller values (left subtree)
2. Visit current node
3. Visit all larger values (right subtree)

The property holds recursively for every subtree, producing a fully sorted sequence.

### Path Through Node vs Path Returned to Parent

**Path Returned to Parent (Diameter / Max Path Sum helper):**
- Maximum path extending from current node downward through ONE child
- Formula: `node.val + max(left, right)`
- Cannot use both children — that would break the path definition
- Used for recursion to build paths in parent nodes

**Path Through Node (Final Answer):**
- Maximum path that uses current node as the "turning point"
- Formula: `node.val + left + right` (uses BOTH children)
- Only valid as a candidate answer, cannot be returned upward
- In Diameter: count edges (`left + right`)
- In Max Path Sum: include node value (`node.val + left + right`)

**Example:**
```
        10
       /  \
      5    15
     / \     \
    3   7     20
```

At node 10:
- Path returned to parent (upward): `10 + max(5-side, 15-side)`
- Path through node 10: `10 + (5-side) + (15-side)` — used for answer only

---

## Checklist

- [x] All 11 problems attempted
- [x] At least 9 problems solved
- [ ] Can write recursive DFS from memory
- [ ] Can write queue-based BFS from memory
- [x] Can explain in-order BST traversal
- [x] Can explain path-through-node vs path-returned-to-parent
