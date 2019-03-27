def dfsLeaves(self, root, leaf_vals):
    if not root: return
    if not (root.left or root.right): # leaf was reached
        leaf_vals.append(root.val)
    self.dfsLeaves(root.left, leaf_vals)
    self.dfsLeaves(root.right, leaf_vals)
        
def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
    leaf_vals1, leaf_vals2 = [], []
    self.dfsLeaves(root1, leaf_vals1)
    self.dfsLeaves(root2, leaf_vals2)
    return leaf_vals1 == leaf_vals2