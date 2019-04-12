def getIntersectionNode(self, headA, headB):
    if not headA or not headB: return None
        
    ha, hb = headA, headB
    while ha != hb:
        ha = ha.next if ha else headB
        hb = hb.next if hb else headA
    return ha