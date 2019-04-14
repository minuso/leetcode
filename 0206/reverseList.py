def reverseList(self, head: ListNode) -> ListNode:
    cur, pre = head, None 
    while cur: 
        nxt_head = cur.next
        cur.next, pre = pre, cur
        cur = nxt_head
    return pre