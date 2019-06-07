def thirdMax(self, nums: List[int]) -> int:
    nums = list(set(nums))
    if len(nums) < 3: return max(nums)
        
    [r3, r2, r1] = sorted(nums[:3])
    for n in nums[3:]:
        if n < r3:
            continue
        if n < r2:
            r3 = n
        elif n < r1:
            r3, r2 = r2, n
        else:
            r3, r2, r1 = r2, r1, n
    return r3