def addTwoNumbers(self, l1, l2):
    res = ListNode(0)
    r, c = res, 0
    while l1 and l2:
        s = l1.val + l2.val + c
        r.next, c = ListNode(s%10), s//10
        l1, l2, r = l1.next, l2.next, r.next

    ll = l1 if l1 else l2
    while ll: # the lengths of l1 and l2 are not equal
        s = ll.val + c
        r.next, c = ListNode(s%10), s//10
        ll, r = ll.next, r.next
        
    if c == 1: # important! c might be 1 after the addition of l1 and l2
        r.next = ListNode(1)
    return res.next