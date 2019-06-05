def sumOfLeftLeaves(self, root: TreeNode) -> int:
    res, stack = 0, [(root, False)] # root is not a left leaf
    while stack:
        node, is_left = stack.pop()
        if node:
            if is_left and not node.left and not node.right:
                res += node.val
                continue
            stack.extend([(node.left, True), (node.right, False)])
    return res