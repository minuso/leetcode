def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    if len(nums1) > len(nums2): return self.intersect(nums2, nums1)
        
    d1 = {n: nums1.count(n) for n in set(nums1)}
    res = []
    for n in nums2:
        if n in d1 and d1[n]:
            res.append(n)
            d1[n] -= 1
    return res