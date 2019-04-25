def preorder(self, root: 'Node') -> List[int]:
    res, stack = [], root and [root] # tip if root is null
    while stack:
        node = stack.pop()
        res.append(node.val)
        stack.extend(reversed(node.children))
    return res