def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
    res, stack = 0, [root]
    while stack:
        node = stack.pop()
        if not node:
            continue
                
        if node.val < L:
            stack.append(node.right)
        elif R < node.val:
            stack.append(node.left)
        else:
            res += node.val
            stack.extend([node.left, node.right])
    return res