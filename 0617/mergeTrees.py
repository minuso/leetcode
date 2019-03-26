def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
    if not t1 and not t2: return None
    if not t1: return t2
    if not t2: return t1
        
    head = TreeNode(t1.val + t2.val)
    head.left = self.mergeTrees(t1.left, t2.left)
    head.right = self.mergeTrees(t1.right, t2.right)
    return head