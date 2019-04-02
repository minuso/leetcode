def convertBST(self, root: TreeNode) -> TreeNode:
    if not root: return None
    # We need to add the final root.val to all nodes in its left subtree,
    # thus a current sum of all greater numbers is needed to be recorded.
    self.total = 0
        
    def toGreaterTree(root):
        if root:
            toGreaterTree(root.right)
            self.total += root.val
            root.val = self.total
            toGreaterTree(root.left)
        return root
        
    return toGreaterTree(root)