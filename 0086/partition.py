def partition(self, head, x):
    sml_head, geq_head = sml, geq = ListNode(0), ListNode(0)
    while head:
        if head.val < x:
            sml.next = head
            sml = sml.next
        else:
            geq.next = head
            geq = geq.next
        head = head.next
            
    sml.next = geq_head.next # connect
    geq.next = None          # important!
    return sml_head.next