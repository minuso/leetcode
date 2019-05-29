def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    pre, end = head, head
    while n:
        end, n = end.next, n-1
    if not end: return head.next # del-head case
        
    while end.next:
        pre, end = pre.next, end.next
    pre.next = pre.next.next
    return head