def postorder(self, root: 'Node') -> List[int]:
    rev, stack = [], root and [root] # tip if root is null
    while stack:
        node = stack.pop()
        rev.append(node.val)
        stack.extend(node.children)
    return list(reversed(rev))