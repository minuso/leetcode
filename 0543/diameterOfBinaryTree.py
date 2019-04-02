def diameterOfBinaryTree(self, root: TreeNode) -> int:
    self.res = 0
    
    def height(root):
        if not root: return 0 # height of each leaf is 1
        hl, hr = height(root.left), height(root.right)
        
        self.res = max(self.res, hl + hr) # maintain longest length
        return max(hl, hr) + 1
        
    height(root)
    return self.res