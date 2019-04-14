def oddEvenList(self, head: ListNode) -> ListNode:
    if not head: return []
        
    odd, even = head, head.next
    even_head = even
    while even and even.next:
        odd.next = odd = even.next
        even.next = even = odd.next
    odd.next = even_head
    return head