def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
    d1 = {r: i for i, r in enumerate(list1)}
        
    res, idx_sum = [], len(list1) + len(list2)
    for i, r in enumerate(list2):
        if r in d1:
            if i + d1[r] > idx_sum:
                continue
                    
            if i + d1[r] < idx_sum:
                res, idx_sum = [r], i + d1[r]
            else:
                res.append(r)
    return res