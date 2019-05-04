def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if p.val > q.val: return self.lowestCommonAncestor(root, q, p)
        
    while root:
        if root.val > q.val:
                root = root.left
        elif root.val < p.val:
            root = root.right
        else:
            return root
    return None