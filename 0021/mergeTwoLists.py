def mergeTwoLists(self, l1, l2):
    res = ptr = ListNode(0)
    while l1:
        if not l2:
            ptr.next = l1
            break
        ptr.next = ListNode(min(l1.val, l2.val))
        ptr = ptr.next
        if l1.val < l2.val: 
            l1 = l1.next
        else: 
            l2 = l2.next
                
    if l2: ptr.next = l2
    return res.next