def inorderTraversal(self, root: TreeNode) -> List[int]:
    res, stack = [], []
    while True:
        while root:
            stack.append(root)
            root = root.left
        if not stack:
            break
        node = stack.pop()
        res.append(node.val) # leftmost nodes: first middle
        root = node.right    # push its right subtree
    return res