def middleNode(self, head: ListNode) -> ListNode:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next      # slower walker takes 1 step
        fast = fast.next.next # faster walker takes 2 steps
    return slow # slower walker is on the middle when the faster to the end