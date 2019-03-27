def searchBST(self, root: TreeNode, val: int) -> TreeNode:
    head = root
    while head and head.val != val:
        head = head.left if head.val > val else head.right
    return head