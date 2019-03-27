def isUnivalTree(self, root: TreeNode) -> bool:
    val = root.val
    stack = [root.left, root.right]
    while stack:
        node = stack.pop()
        if node:
            if node.val != val:
                return False
            stack.extend([node.left, node.right]) # list.extend() is used to append multiple values
    return True