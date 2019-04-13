def kthSmallest(self, root: TreeNode, k: int) -> int:
    stack = [root]
    while stack[-1].left:
        stack.append(stack[-1].left)
            
    res = TreeNode(0)
    while k:
        res, k = stack.pop(), k-1
        rt = res.right       # nodes in the right subtree of the leftmost node (res)
        while rt:            # are all smaller than the parent node of res
            stack.append(rt)
            rt = rt.left
    return res.val