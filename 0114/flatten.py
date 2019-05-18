def flatten(self, root):
    if not root: return None
        
    stack = [root]
    while stack:
        node = stack.pop()
        if node.right: stack.append(node.right) # push right first!
        if node.left:  stack.append(node.left)
        node.left = None
        node.right = stack[-1] if stack else None