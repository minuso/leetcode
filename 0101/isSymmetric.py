def isSymmetric(self, root):
    if not root: return True
        
    def isMirror(t1, t2):
        if not t1 and not t2: return True
        if not t1 or not t2: return False
        if t1.val != t2.val: return False
            
        in_mirror = isMirror(t1.right, t2.left)
        out_mirror = isMirror(t1.left, t2.right)
        return in_mirror and out_mirror
        
    return isMirror(root.left, root.right)