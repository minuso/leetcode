def insertIntoBST(self, root, val):
    if not root: return TreeNode(val)
        
    node = root
    while node:
        if node.val > val:
            if not node.left:
                node.left = TreeNode(val)
                break
            node = node.left
        else:
            if not node.right:
                node.right = TreeNode(val)
                break
            node = node.right
    return root