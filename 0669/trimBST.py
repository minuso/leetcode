def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
    if not root: return None
        
    if root.val < L:
        return self.trimBST(root.right, L, R)
    if R < root.val:
        return self.trimBST(root.left, L, R)
        
    root.right = self.trimBST(root.right, L, R)
    root.left = self.trimBST(root.left, L, R)
    return root