def levelOrder(self, root: TreeNode) -> List[List[int]]:
    res, queue = [], [root]
    while queue:
        vs, ns = [], []
        for n in queue:
            if n:
                vs.append(n.val)
                ns.extend([n.left, n.right])
        res.append(vs)
        queue = ns
    return res[:len(res)-1] # the last level is empty