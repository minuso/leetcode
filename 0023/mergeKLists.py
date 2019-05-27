def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    if not lists: return None
        
    while len(lists) != 1:
        new_lists = []
        if len(lists)&1: lists.append([]) # keep len(lists) even
        for i in range(0, len(lists), 2):
            new_lists.append(self.merge(lists[i], lists[i+1]))
        lists = new_lists
    return lists[0]

def merge(self, p1, p2):
    r_head = r = ListNode(0)
    while p1 and p2:
        if p1.val < p2.val:
            r.next, p1 = p1, p1.next
        else:
            r.next, p2 = p2, p2.next
        r = r.next
    r.next = p1 or p2
    return r_head.next