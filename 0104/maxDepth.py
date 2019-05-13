def maxDepth(self, root):
    if not root: return 0
        
    res = 0
    stack = [root]
    while stack:
        res += 1
        vs, stack = stack, []
        for v in vs:
            if v.left:  stack.append(v.left)
            if v.right: stack.append(v.right)
    return res