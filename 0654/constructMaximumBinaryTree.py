def constructMaximumBinaryTree(self, nums):
    if not nums: return None
        
    stack = []
    for v in nums:
        node = TreeNode(v)
        while stack and stack[-1].val < v:
            node.left = stack.pop() # past smaller node
        if stack:
            stack[-1].right = node  # past bigger node
        stack.append(node)
    return stack[0]