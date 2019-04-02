def isSameTree(self, t1, t2):
    if not t1 and not t2: return True
    if not t1 or not t2: return False
    if t1.val != t2.val: return False
    return self.isSameTree(t1.left, t2.left) and self.isSameTree(t1.right, t2.right)
        
def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
    # recursive
    if self.isSameTree(s, t): return True
    if s:
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t) 
    return False
    '''
    # iterative
    stack = [s]
    while stack:
        root = stack.pop()
        if self.isSameTree(root, t):
            return True
        if root:
            stack.extend((root.left, root.right))
    return False
    '''