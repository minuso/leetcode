def maxDepth(self, root: 'Node') -> int:
    if not root: return 0
        
    res, layer = 0, [root]
    while layer:
        res, tmp = res+1, []
        for node in layer:
            tmp.extend(node.children)
        layer = tmp
    return res