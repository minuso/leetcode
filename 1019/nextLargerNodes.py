def nextLargerNodes(self, head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
        
    stack = []
    for i in range(len(res) - 1, -1, -1):
        v = res[i]
        while stack and stack[-1] <= v:
            stack.pop()
                
        res[i] = 0 if not stack else stack[-1]
        stack.append(v)
    return res